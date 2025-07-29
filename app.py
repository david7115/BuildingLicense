import pandas as pd
import json
import glob
import os

def load_and_convert():
    raw_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    raw_dir = os.path.abspath(raw_dir)

    bdong_path = glob.glob(os.path.join(raw_dir, "KIKcd_B*.xlsx"))[0]
    hdong_path = glob.glob(os.path.join(raw_dir, "KIKcd_H*.xlsx"))[0]
    mix_path = glob.glob(os.path.join(raw_dir, "KIKmix*.xlsx"))[0]

    bdong = pd.read_excel(bdong_path, dtype=str)
    hdong = pd.read_excel(hdong_path, dtype=str)
    mix = pd.read_excel(mix_path, dtype=str)

    bdong['시도코드'] = bdong['법정동코드'].str[:2]
    bdong['시군구코드'] = bdong['법정동코드'].str[:5]
    bdong = bdong[['시도코드','시도명','시군구코드','시군구명',
                   '법정동코드','읍면동명','동리명','생성일자','말소일자']]

    hdong['시도코드'] = hdong['행정동코드'].str[:2]
    hdong['시군구코드'] = hdong['행정동코드'].str[:5]
    hdong = hdong[['시도코드','시도명','시군구코드','시군구명',
                   '행정동코드','읍면동명','생성일자','말소일자']]

    mix['시도코드'] = mix['행정동코드'].str[:2]
    mix['시군구코드'] = mix['행정동코드'].str[:5]
    mix = mix[['시도코드','시도명','시군구코드','시군구명',
               '행정동코드','읍면동명','법정동코드','동리명','생성일자','말소일자']]

    bdong.to_json(os.path.join(raw_dir, "code_bdong.json"), force_ascii=False, indent=2)
    hdong.to_json(os.path.join(raw_dir, "code_hdong.json"), force_ascii=False, indent=2)
    mix.to_json(os.path.join(raw_dir, "code_hdong_bdong.json"), force_ascii=False, indent=2)

    print("✅ JSON 파일 저장 완료")

if __name__ == "__main__":
    load_and_convert()
