from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from datetime import datetime


def generate_pdf_report(
    filename,
    df,
    info,
    statistics,
    insights=None
):

    document = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=15,
        leading=20,
        spaceBefore=10,
        spaceAfter=10
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13
    )

    story = []


    # =================================================
    # TITLE
    # =================================================

    story.append(
        Paragraph(
            "AI Data Analysis Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            "AI Data Analysis Assistant",
            subtitle_style
        )
    )

    story.append(
        Paragraph(
            f"Generated on: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            subtitle_style
        )
    )

    story.append(
        Spacer(1, 10)
    )


    # =================================================
    # EXECUTIVE SUMMARY
    # =================================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    total_missing = sum(
        info["missing_values"].values()
    )

    duplicate_rows = int(
        df.duplicated().sum()
    )

    summary_text = (
        f"This dataset contains "
        f"<b>{info['rows']}</b> rows and "
        f"<b>{info['columns']}</b> columns. "
        f"It contains <b>{total_missing}</b> missing values "
        f"and <b>{duplicate_rows}</b> duplicate rows."
    )

    story.append(
        Paragraph(
            summary_text,
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # =================================================
    # DATASET OVERVIEW
    # =================================================

    story.append(
        Paragraph(
            "Dataset Overview",
            heading_style
        )
    )

    overview_data = [
        ["Metric", "Value"],
        ["Rows", str(info["rows"])],
        ["Columns", str(info["columns"])],
        ["Duplicate Rows", str(duplicate_rows)],
        ["Total Missing Values", str(total_missing)]
    ]

    overview_table = Table(
        overview_data,
        colWidths=[3 * inch, 2 * inch]
    )

    overview_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.black
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                7
            )
        ])
    )

    story.append(
        overview_table
    )

    story.append(
        Spacer(1, 20)
    )


    # =================================================
    # COLUMN INFORMATION
    # =================================================

    story.append(
        Paragraph(
            "Column Information",
            heading_style
        )
    )

    column_data = [
        ["Column", "Data Type"]
    ]

    for column in df.columns:

        column_data.append([
            str(column),
            str(df[column].dtype)
        ])

    column_table = Table(
        column_data,
        colWidths=[3.5 * inch, 2 * inch],
        repeatRows=1
    )

    column_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(
        column_table
    )

    story.append(
        Spacer(1, 20)
    )


    # =================================================
    # MISSING VALUES
    # =================================================

    story.append(
        Paragraph(
            "Missing Values",
            heading_style
        )
    )

    missing_data = [
        ["Column", "Missing Values"]
    ]

    for column, value in info["missing_values"].items():

        missing_data.append([
            str(column),
            str(value)
        ])

    missing_table = Table(
        missing_data,
        colWidths=[3.5 * inch, 2 * inch],
        repeatRows=1
    )

    missing_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(
        missing_table
    )

    story.append(
        Spacer(1, 20)
    )


    # =================================================
    # BASIC STATISTICS
    # =================================================

    story.append(
        Paragraph(
            "Basic Statistics",
            heading_style
        )
    )

    statistics_text = statistics.to_string()

    # Escape special HTML characters
    statistics_text = (
        statistics_text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )

    story.append(
        Paragraph(
            f"<font name='Courier' size='7'>"
            f"{statistics_text}"
            f"</font>",
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # =================================================
    # AI INSIGHTS
    # =================================================

    if insights:

        story.append(
            Paragraph(
                "AI Dataset Insights",
                heading_style
            )
        )

        formatted_insights = (
            str(insights)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "<br/>")
        )

        story.append(
            Paragraph(
                formatted_insights,
                body_style
            )
        )

        story.append(
            Spacer(1, 20)
        )


    # =================================================
    # FOOTER / FINAL NOTE
    # =================================================

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "Generated using AI Data Analysis Assistant",
            subtitle_style
        )
    )


    # =================================================
    # BUILD PDF
    # =================================================

    document.build(story)