import streamlit as st

from question_answering import answer_question
from analysis import load_data, get_dataset_info, get_basic_statistics
from ai_explanation import generate_explanation


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="🤖",
    layout="wide"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🤖 AI Data Analysis Assistant")

st.write(
    "Upload a CSV file and let AI analyze your dataset, "
    "generate insights, and answer your questions."
)


# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Choose a CSV file",
    type=["csv"]
)


# -------------------------------------------------
# MAIN APPLICATION
# -------------------------------------------------

if uploaded_file is not None:

    # Load dataset
    df = load_data(uploaded_file)

    # -------------------------------------------------
    # DATASET PREVIEW
    # -------------------------------------------------

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    # -------------------------------------------------
    # DATASET INFORMATION
    # -------------------------------------------------

    info = get_dataset_info(df)

    st.subheader("📊 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    # Rows
    col1.metric(
        "Rows",
        info["rows"]
    )

    # Columns
    col2.metric(
        "Columns",
        info["columns"]
    )

    # Missing values
    missing_values = info["missing_values"]

    total_missing = sum(
        missing_values.values()
    )

    col3.metric(
        "Missing Values",
        total_missing
    )

    # Duplicate rows
    duplicate_rows = int(
        df.duplicated().sum()
    )

    col4.metric(
        "Duplicate Rows",
        duplicate_rows
    )

    # -------------------------------------------------
    # COLUMN NAMES
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

    statistics = get_basic_statistics(df)

    st.dataframe(
        statistics,
        use_container_width=True
    )

    # -------------------------------------------------
    # ASK YOUR DATASET
    # -------------------------------------------------

    st.subheader("💬 Ask Your Dataset")

    question = st.text_input(
        "Ask something about your dataset:",
        placeholder="Example: Which product generated the highest sales?"
    )

    if question:

        # AI is processing
        with st.spinner(
            "🤖 Analyzing your dataset..."
        ):

            answer = answer_question(
                df,
                question
            )

        # -------------------------------------------------
        # ANSWER
        # -------------------------------------------------

        st.subheader("💡 Answer")

        st.success(answer)

        # -------------------------------------------------
        # AI EXPLANATION
        # -------------------------------------------------

        st.subheader("🤖 AI Explanation")

        with st.spinner(
            "Generating explanation..."
        ):

            explanation = generate_explanation(
                answer
            )

        st.write(explanation)


# -------------------------------------------------
# NO FILE UPLOADED
# -------------------------------------------------

else:

    st.info(
        "👆 Upload a CSV file above to start analyzing your dataset."
    )