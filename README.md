#CSV Profiler
Generate a profiling report for a csv file
#features
-CLI: JSON + Markdown report
-Streamlit GUI: upload CSV + export reports
#setup
uv venv -p 3.11
uv pip install -r requirements.txt
uv run install streamlit


##run CLI 
# If you have a src? folder:
#Mac/Linux: export PYTHONPATH=src
#Windows:  $env:PYTHONPATH="src"
uv run python -m csv_profiler.cli data/sample.csv --out-dir outputs

##Run GUI
# if you have a src/ folder:
##windows: $env:PYTHONPATH="src"
 uv run streamlit run src/csv_profiler/app.py
# output files 
the cli writes:
output/report.JSON
output/report.Markdown

also the streamlit app can:
-preview the report
-download GSON + Markdown

![streamlit UI](images/app_preview.png)
![streamlit UI](images/app_preview1.png)
![streamlit UI](images/app_preview3.png)
![streamlit UI](images/app_preview4.png)