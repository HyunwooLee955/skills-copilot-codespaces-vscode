import pooch
import pandas as pd

kodc_url = r"https://www.nifs.go.kr/OpenAPI_json?id=sooList"
key = "qPwOeIrU-2501-PXXKVD-1011"
sdate = "19680101"
edate = "20241231"

fname_soo = pooch.retrieve(
    url=f"https://www.nifs.go.kr/OpenAPI_json?id=sooList&key={key}&sdate={sdate}&edate={edate}",
    known_hash=None,
)

data_soo = pd.read_json(fname_soo, orient="records")