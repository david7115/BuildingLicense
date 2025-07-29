import pandas as pd
import os

output_dir = os.path.join("data", "raw")
os.makedirs(output_dir, exist_ok=True)

# 1. 법정동 코드 샘플
df_bdong = pd.DataFrame({
    '법정동코드': ['1111010100', '1111010200'],
    '시도명': ['서울특별시', '서울특별시'],
    '시군구명': ['종로구', '종로구'],
    '읍면동명': ['청운효자동', '사직동'],
    '동리명': ['청운동', '사직동'],
    '생성일자': ['20220101', '20220101'],
    '말소일자': [None, None]
})
df_bdong.to_excel(os.path.join(output_dir, 'KIKcd_B_sample.xlsx'), index=False)

# 2. 행정동 코드 샘플
df_hdong = pd.DataFrame({
    '행정동코드': ['1101053', '1101054'],
    '시도명': ['서울특별시', '서울특별시'],
    '시군구명': ['종로구', '종로구'],
    '읍면동명': ['청운효자동', '사직동'],
    '생성일자': ['20220101', '20220101'],
    '말소일자': [None, None]
})
df_hdong.to_excel(os.path.join(output_dir, 'KIKcd_H_sample.xlsx'), index=False)

# 3. 혼합코드 (행정동 ↔ 법정동 매핑)
df_mix = pd.DataFrame({
    '행정동코드': ['1101053', '1101054'],
    '시도명': ['서울특별시', '서울특별시'],
    '시군구명': ['종로구', '종로구'],
    '읍면동명': ['청운효자동', '사직동'],
    '법정동코드': ['1111010100', '1111010200'],
    '동리명': ['청운동', '사직동'],
    '생성일자': ['20220101', '20220101'],
    '말소일자': [None, None]
})
df_mix.to_excel(os.path.join(output_dir, 'KIKmix_sample.xlsx'), index=False)

print("✅ 샘플 파일 3개가 생성되었습니다.")
