#CSV Profiler
Generate a profiling report for a csv file
#features
-CLI: JSON + Markdown report
-Streamlit GUI: upload CSV + export reports
#setup
uv venv -p 3.11
uv pip install -r requirements.txt
uv run install streamlit
uv run python -m csv_profiler.cli data/sample.csv --out-dir outputs

##run CLI 
# If you have a src? folder:
#Mac/Linux: export PYTHONPATH=src
#Windows: $env: PYTHONPATH="src"
uv run python -m csv_profiler.cli profile data/sample.csv --out-dir outputs
##Run GUI
# if you have a src/ folder:
# output files 
the cli writes:
output/report.JSON
output/report.Markdown

also the streamlit app can:
-preview the report
-download GSON + Markdown

![streamlit UI](images/ui.png)