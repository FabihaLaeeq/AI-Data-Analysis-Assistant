import streamlit as st

from question_answering import answer_question
from analysis import (
    load_data,
    get_dataset_info,
    get_basic_statistics
)

from ai_explanation import (
    generate_explanation,
    generate_dataset_insights
)

from visualization import (
    sales_by_product,
    numerical_histogram,
    box_plot,
    correlation_heatmap,
    scatter_plot
)

from report_generator import generate_pdf_report


# =================================================
# PAGE CONFIGURATION
# =================================================

st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="🤖",
    layout="wide"
)


# =================================================
# CUSTOM STYLING
# =================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f9fc;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 30px;
    }

    div[data-testid="metric-container"] {
        background-color: white;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 10px;
    }

    .stDownloadButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =================================================
# TITLE
# =================================================

st.markdown(
    '<div class="main-title">'
    '🤖 AI Data Analysis Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Turn your CSV data into insights, visualizations, '
    'and AI-powered answers.'
    '</div>',
    unsafe_allow_html=True
)


# =================================================
# FILE UPLOAD
# =================================================

st.subheader("📂 Upload Your Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file to begin analysis",
    type=["csv"],
    help="Upload a CSV dataset for automatic analysis."
)


# =================================================
# MAIN APPLICATION
# =================================================

if uploaded_file is not None:

    # =================================================
    # LOAD DATA SAFELY
    # =================================================

    try:

        df = load_data(uploaded_file)

    except ValueError as e:

        st.error(f"❌ {e}")
        st.stop()

    except Exception:

        st.error(
            "❌ Something went wrong while loading "
            "the CSV file."
        )

        st.stop()


    # =================================================
    # DATASET INFORMATION
    # =================================================

    info = get_dataset_info(df)

    statistics = get_basic_statistics(df)

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    missing_values = info["missing_values"]


    # =================================================
    # SESSION STATE
    # =================================================

    if "insights" not in st.session_state:

        st.session_state.insights = None


    # =================================================
    # TABS
    # =================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Overview",
            "📈 Visualizations",
            "🧠 AI Insights",
            "💬 Ask Dataset",
            "📕 Report"
        ]
    )


    # =================================================
    # TAB 1: OVERVIEW
    # =================================================

    with tab1:

        st.subheader("📋 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )


        # -------------------------------------------------
        # DATASET OVERVIEW
        # -------------------------------------------------

        st.subheader("📊 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)


        col1.metric(
            "Rows",
            info["rows"]
        )


        col2.metric(
            "Columns",
            info["columns"]
        )


        total_missing = sum(
            missing_values.values()
        )

        col3.metric(
            "Missing Values",
            total_missing
        )


        duplicate_rows = int(
            df.duplicated().sum()
        )

        col4.metric(
            "Duplicate Rows",
            duplicate_rows
        )


        # -------------------------------------------------
        # COLUMN INFORMATION
        # -------------------------------------------------

        st.subheader("🧾 Column Information")

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Column Names:**")

            st.write(
                info["column_names"]
            )

        with col2:

            st.write("**Data Types:**")

            st.write(
                info["data_types"]
            )


        # -------------------------------------------------
        # MISSING VALUES
        # -------------------------------------------------

        st.subheader("❌ Missing Values")

        missing_table = {
            "Column": list(
                missing_values.keys()
            ),
            "Missing Values": list(
                missing_values.values()
            )
        }

        st.dataframe(
            missing_table,
            use_container_width=True
        )


        # -------------------------------------------------
        # BASIC STATISTICS
        # -------------------------------------------------

        st.subheader("📈 Basic Statistics")

        st.dataframe(
            statistics,
            use_container_width=True
        )


    # =================================================
    # TAB 2: VISUALIZATIONS
    # =================================================

    with tab2:

        st.subheader("📊 Data Visualizations")


        # -------------------------------------------------
        # SALES BY PRODUCT
        # -------------------------------------------------

        if (
            "Product" in df.columns
            and "Sales" in df.columns
        ):

            st.write("### 💰 Sales by Product")

            try:

                sales_chart = sales_by_product(df)

                if sales_chart is not None:

                    st.plotly_chart(
                        sales_chart,
                        use_container_width=True
                    )

            except Exception:

                st.warning(
                    "⚠️ Could not generate the "
                    "Sales by Product chart."
                )


        # -------------------------------------------------
        # NUMERICAL DISTRIBUTION
        # -------------------------------------------------

        if numeric_columns:

            st.write(
                "### 📈 Numerical Distributions"
            )

            selected_column = st.selectbox(
                "Select a numerical column:",
                numeric_columns,
                key="histogram_column"
            )

            try:

                histogram = numerical_histogram(
                    df,
                    selected_column
                )

                if histogram is not None:

                    st.plotly_chart(
                        histogram,
                        use_container_width=True
                    )

            except Exception:

                st.warning(
                    "⚠️ Could not generate "
                    "the histogram."
                )


        # -------------------------------------------------
        # BOX PLOT
        # -------------------------------------------------

        if numeric_columns:

            st.write(
                "### 📦 Outlier Detection"
            )

            box_column = st.selectbox(
                "Select a column for box plot:",
                numeric_columns,
                key="box_plot_column"
            )

            try:

                box = box_plot(
                    df,
                    box_column
                )

                if box is not None:

                    st.plotly_chart(
                        box,
                        use_container_width=True
                    )

            except Exception:

                st.warning(
                    "⚠️ Could not generate "
                    "the box plot."
                )


        # -------------------------------------------------
        # CORRELATION HEATMAP
        # -------------------------------------------------

        if len(numeric_columns) >= 2:

            st.write(
                "### 🔥 Correlation Analysis"
            )

            try:

                heatmap = correlation_heatmap(df)

                if heatmap is not None:

                    st.plotly_chart(
                        heatmap,
                        use_container_width=True
                    )

            except Exception:

                st.warning(
                    "⚠️ Could not generate "
                    "the correlation heatmap."
                )


        # -------------------------------------------------
        # SCATTER PLOT
        # -------------------------------------------------

        if len(numeric_columns) >= 2:

            st.write(
                "### 🔵 Relationship Between Variables"
            )

            col1, col2 = st.columns(2)


            with col1:

                x_column = st.selectbox(
                    "X-axis:",
                    numeric_columns,
                    key="scatter_x"
                )


            with col2:

                y_column = st.selectbox(
                    "Y-axis:",
                    numeric_columns,
                    key="scatter_y"
                )


            if x_column != y_column:

                try:

                    scatter = scatter_plot(
                        df,
                        x_column,
                        y_column
                    )

                    if scatter is not None:

                        st.plotly_chart(
                            scatter,
                            use_container_width=True
                        )

                except Exception:

                    st.warning(
                        "⚠️ Could not generate "
                        "the scatter plot."
                    )

            else:

                st.info(
                    "Please select two different "
                    "columns for the scatter plot."
                )


        if not numeric_columns:

            st.info(
                "This dataset does not contain "
                "numerical columns for visualization."
            )


    # =================================================
    # TAB 3: AI INSIGHTS
    # =================================================

    with tab3:

        st.subheader("🧠 AI Dataset Insights")

        st.write(
            "Let AI examine your dataset and identify "
            "important patterns and findings."
        )


        if st.button(
            "🔍 Generate AI Insights",
            key="generate_insights"
        ):

            with st.spinner(
                "🤖 AI is analyzing your dataset..."
            ):

                try:

                    st.session_state.insights = (
                        generate_dataset_insights(df)
                    )

                except Exception:

                    st.session_state.insights = None

                    st.error(
                        "❌ AI could not analyze the "
                        "dataset right now. Please check "
                        "your Gemini API key and try again."
                    )


        if st.session_state.insights:

            st.success(
                "AI analysis completed!"
            )

            st.write(
                st.session_state.insights
            )

        else:

            st.info(
                "Click the button above to generate "
                "AI-powered insights."
            )


    # =================================================
    # TAB 4: ASK YOUR DATASET
    # =================================================

    with tab4:

        st.subheader("💬 Ask Your Dataset")

        st.write(
            "Ask a question about the uploaded dataset "
            "and get an AI-powered answer."
        )


        question = st.text_input(
            "Ask something about your dataset:",
            placeholder=(
                "Example: Which product generated "
                "the highest sales?"
            ),
            key="dataset_question"
        )


        # -------------------------------------------------
        # QUESTION PROCESSING
        # -------------------------------------------------

        if question:

            with st.spinner(
                "🤖 Analyzing your dataset..."
            ):

                try:

                    answer = answer_question(
                        df,
                        question
                    )

                except Exception:

                    answer = (
                        "Sorry, I could not process that "
                        "question. Please check your dataset "
                        "columns and try again."
                    )


            # -------------------------------------------------
            # ANSWER
            # -------------------------------------------------

            st.subheader("💡 Answer")

            st.success(
                answer
            )


            # -------------------------------------------------
            # AI EXPLANATION
            # -------------------------------------------------

            st.subheader("🤖 AI Explanation")

            with st.spinner(
                "Generating explanation..."
            ):

                try:

                    explanation = generate_explanation(
                        answer
                    )

                except Exception:

                    explanation = (
                        "AI explanation is currently "
                        "unavailable. The answer above "
                        "was generated successfully."
                    )


            st.write(
                explanation
            )


    # =================================================
    # TAB 5: PDF REPORT
    # =================================================

    with tab5:

        st.subheader(
            "📕 Download Analysis Report"
        )

        st.write(
            "Generate a PDF containing your dataset "
            "analysis, statistics, and AI insights."
        )


        if st.session_state.insights:

            st.success(
                "✅ AI insights will be included "
                "in the report."
            )

        else:

            st.info(
                "💡 Generate AI Insights first if you "
                "want them included in the PDF."
            )


        # -------------------------------------------------
        # GENERATE PDF
        # -------------------------------------------------

        if st.button(
            "📄 Generate PDF Report",
            key="generate_pdf"
        ):

            pdf_filename = (
                "ai_dataset_analysis_report.pdf"
            )


            try:

                with st.spinner(
                    "📄 Creating your PDF report..."
                ):

                    generate_pdf_report(
                        pdf_filename,
                        df,
                        info,
                        statistics,
                        st.session_state.insights
                    )


                with open(
                    pdf_filename,
                    "rb"
                ) as pdf_file:

                    pdf_data = pdf_file.read()


                st.session_state.pdf_data = pdf_data


                st.success(
                    "✅ PDF report generated successfully!"
                )


            except Exception as e:

                st.error(
                    "❌ Could not generate the PDF report."
                )


        # -------------------------------------------------
        # DOWNLOAD PDF
        # -------------------------------------------------

        if "pdf_data" in st.session_state:

            st.download_button(
                label="⬇️ Download PDF Report",
                data=st.session_state.pdf_data,
                file_name=(
                    "ai_dataset_analysis_report.pdf"
                ),
                mime="application/pdf",
                key="download_pdf"
            )


# =================================================
# NO FILE UPLOADED
# =================================================

else:

    st.info(
        "👆 Upload a CSV file above to start "
        "analyzing your dataset."
    )

    st.markdown(
        """
        ### 🚀 What this app can do

        **📊 Dataset Analysis**
        - Preview your dataset
        - Show rows and columns
        - Detect missing values
        - Detect duplicate rows
        - Generate statistics

        **📈 Visualizations**
        - Sales by product
        - Numerical distributions
        - Box plots
        - Correlation heatmap
        - Scatter plots

        **🧠 AI Features**
        - Generate dataset insights
        - Ask questions about your data
        - Get beginner-friendly explanations

        **📕 Reporting**
        - Generate a PDF analysis report
        - Download your results
        """
    )