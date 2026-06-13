from reports.daily_report_generator import (
    daily_report
)


def generate_pdf_data():

    report = (
        daily_report()
    )

    return report