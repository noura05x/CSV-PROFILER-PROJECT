import csv
import json
from pathlib import Path
import streamlit as st
from io import StringIO
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Upload a CSV → profile it → export JSON + Markdown")
st.sidebar.header("Input")
rows = None
report = st.session_state.get("report")


uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.checkbox("Show preview", value=True)

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

    if show_preview:
        st.subheader("preview")
        st.write(rows[:5])
else:
    st.info("Upload a CSV to begin.")

if rows is not None:
     if len(rows)>0:
          if st.button("generate report"):
               st.session_state["report"] = profile_rows(rows)

report = st.session_state.get("report")
if report is not None:
     cols = st.columns(2)
     cols[0].metric("Rows", report["n_rows"])
     cols[1].metric("Columns", report["n_cols"])


if report is not None:
     st.subheader("Show Columns table")
     st.write(report["columns"])
     with st.expander("Markdown preview", expanded=False):
          st.markdown(render_markdown(report))

if report is not None:
     report_name = st.sidebar.text_input("Report name", value="report")
     json_file = report_name + ".json"
     json_text = json.dumps(report, indent=2, ensure_ascii=False)

     md_file = report_name + ".md"
     md_text = render_markdown(report) 
     c1, c2 = st.columns(2)
     c1.download_button("Download JSON", data=json_text, file_name=json_file)
     c2.download_button("Download Markdown", data=md_text, file_name=md_file)

     if st.button("save to output/"):
          out_dir = Path("output")
          out_dir.mkdir(parents=True, exist_ok=True)
          (out_dir / json_file).write_text(json_text, encoding="utf-8")
          (out_dir / md_file).write_text(md_text, encoding="utf-8")
          st.success("saved outputs/" + json_file + "and outputs/" + md_file)

if uploaded is not None:
     text = uploaded.getvalue().decode("utf-8-sig")
     rows = list(csv.DictReader(StringIO(text)))
     if len(rows) == 0:
          st.error("CSV has no data")
          st.stop()
     if len(rows[0]) == 0:
          st.warning("CSV has no headers")
    