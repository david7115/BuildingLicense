import streamlit as st
import pandas as pd
from PublicDataReader import BuildingLicense

# ✅ 디코딩된 서비스 키 적용
SERVICE_KEY = "ZarTYb88UP8FCrJp2W+Wxiu4ffdIgJluH8tBA8FKMt553Y+PuBf/2Cxi61wxKU/GfGdeINYC8KuofirJkyf0rA=="

# API 인스턴스 생성
api = BuildingLicense(SERVICE_KEY)

# Streamlit 기본 설정
st.set_page_config(page_title="건축허가정보 조회", layout="wide")
st.title("🏗️ 건축허가정보 서비스 (국토교통부 건축HUB)")

# 🔍 사용자 입력
with st.sidebar:
    st.header("🔧 조회조건")
    service_type = st.selectbox("서비스유형", ["기본개요", "동별개요", "층별개요", "호별개요", "대수선", "주차장"])
    sigungu_code = st.text_input("시군구코드 (예: 41135)", value="41135")
    bdong_code = st.text_input("법정동코드 (예: 11000)", value="11000")
    search = st.button("🔍 조회 실행")

# 🚀 데이터 조회
if search:
    with st.spinner("📡 건축정보를 조회 중입니다..."):
        try:
            df = api.get_data(
                service_type=service_type,
                sigungu_code=sigungu_code,
                bdong_code=bdong_code,
                plat_code=None,
                bun=None,
                ji=None,
                translate=True,
                verbose=False
            )

            if not df.empty:
                st.success(f"✅ {len(df)}건의 결과를 조회했습니다.")
                st.dataframe(df, use_container_width=True)

                # 📥 CSV 다운로드
                csv = df.to_csv(index=False).encode('utf-8-sig')
                st.download_button("📁 CSV 다운로드", csv, "building_license.csv", "text/csv")
            else:
                st.warning("📭 해당 조건에 맞는 건축허가 데이터가 없습니다.")

        except Exception as e:
            st.error(f"🚨 API 호출 실패: {e}")

