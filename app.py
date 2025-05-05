import streamlit as st
from scraper import scrape_jobs

st.title("Station F Job Board Scraper")

pages = st.number_input("Number of pages to scrape", min_value=1, max_value=10, value=2)

if st.button("Scrape Jobs"):
    with st.spinner("Scraping in progress..."):
        df = scrape_jobs(pages)
        st.success("Scraping completed!")
        st.dataframe(
            df,
            column_config={
                "Job Link": st.column_config.LinkColumn("Job Link")
            }
        )
        df.to_excel('stationf_jobs.xlsx', index=False)
        st.download_button(
            label="Download Excel file",
            data=open('stationf_jobs.xlsx', 'rb'),
            file_name='stationf_jobs.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
