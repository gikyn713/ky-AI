import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
from to import BytesIO
def get_exchange(currency_code):
    last_page_num = 10
    df = pd.DataFrame()

for page_no in range(1,4):
    url= f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{currency_code}KRW&page={page_no}"
    dfs = pd.read_html(url,header=1,encoding='cp949')

    if dfs[0].empty:
        if (page_no == 1):
            print(f"통화코드{}가 잘못 지정되었습니다")
        else:
            print(f"{}마지막 페이지입니다.")
        break

    # print(dfs[0])
    df = pd.concat([df,dfs[0]],ignore_index=False)


currency_name_dict={'미국달러':'USD','유럽연합 유로':'EUR','일본 엔':'jpy'}
st.sidebar.selectbox('통화선택',)
clicked = st.sidebar.button("환율 데이터 가져오기")

if clicked:
    currency_code = currency_name_dict[currency_name]
    df_exchange = ger_exchange(currency_code)



    # 원하는 열만 선택
    df_exchange_rate = df_exchange[['']]
    df_exchange_rate2= df_exchange_rate.set_index('')
    
    # 날짜열의 테이터 변경
    df_exchange_rate2.index=pd.to_datetime()

    # 환율 데이터 표시
    st.subheader(f"{currency_name}")
    st.dataframe(df_exchange_rate2.head(20))

    # 챠트 (선 그래프) 그리기
    matplotlib.rc_params['font.family']='Malgun Gothic'
    ax = df_exchange_rate2[''].plot(figsize=(15,5),grid=True)
    ax.set_title("()",figsize=20)
    ax.set_xlabel("",figsize=10)
    ax.set_ylabel(f"/{}",figsize=10)
    plt.ticks(figsize=)    # x 축 눈금값의 폰트 크기
    plt.ticks(figsize=)
    fig = ax.get_figure()  # fig 객체 가져오기
    st.pyplot

    st.text("**  **")

    csv_data = df_exchange_rate.to_csv()


    excel_data = BytesIO()
    df_exchange_rate.to_excel()

    col = st.columns(2)
    with col[0]:
        st.download_button("csv 파일 다운로드")
     with col[0]:
        st.download_button("")    
    
