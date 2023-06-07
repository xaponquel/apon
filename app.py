import streamlit as st
import pandas as pd
import plotly_express as px


st.set_page_config(layout='wide')
st.header('Blog Stats Dashboard')


#Awal Support Function
def calculate_differences(df): #untuk menghitung selisih
    #menghitung selisih current month and previous month untuk kolom followers,email_subs,referred_members
    #df['nama_kolom'].diff() menghitung selisih dan membuat kolom baru untuk menyimpan selisihnya 
    df['followers_increase'] = df['followers'].diff()
    df['email_subs_increase'] = df['email_subs'].diff()
    df['referred_members_increase'] = df['referred_members'].diff()
    return df

#untuk mencari nilai tiap kolom pada baris terakhir
def get_latest_monthly_metrics(df):

    df['date'] = pd.to_datetime(df['date']) #mengubah text menjadi tanggal beneran
    df['month'] = df['date'].dt.month_name() #mengambil nama bulan
    
    latest_month = df['month'].iloc[-1] #mengambil nilai month di baris terakhir
    
    
    latest_follower_count = [ 
                            df['followers'].iloc[-1], #mencari nilai follower pada baris terakhir
                            df['followers_increase'].iloc[-1] #mencari nilai perubahan follower pada baris terakhir
                             ]
    
    latest_sub_count = [
                        df['email_subs'].iloc[-1], #mencari nilai subscriber pada baris terakhir
                        df['email_subs_increase'].iloc[-1] #mencari nilai perubahan subscriber pada baris terakhir
                        ]
    
    latest_refs_count = [
                        df['referred_members'].iloc[-1], #mencari nilai referral pada baris terakhir 
                        df['referred_members_increase'].iloc[-1] #mencari nilai perubahan referral pada baris terakhir
                        ]

    return latest_month, latest_follower_count, latest_sub_count, latest_refs_count

#untuk updata data csv
def update_stats_csv(date, followers, email_subs, ref_members):
    with open('data.csv', 'a+') as f:
        f.write(f'\n{date},{followers},{email_subs},{ref_members}')
#Akhir Support Function


#Mulai Sidebar
with st.sidebar.form('Enter the latest stats from your Medium dashboard'):

    date = st.date_input('Date')
    
    follower_num = st.number_input('Followers', step=1)
    email_subs = st.number_input('Email Subscribers', step=1)
    ref_members = st.number_input('Referred Members', step=1)

    submit_stats = st.form_submit_button('Write Stats to CSV')

    if submit_stats:
        #kalau button diklik, kodingan ini akan dijalankan
        update_stats_csv(date, follower_num, email_subs, ref_members)
        st.info(f'Stats for {date} have been added to the csv file')
#Akhir Sidebar


#Awal halaman utama
df = pd.read_csv('data.csv')   #untuk membaca file data
df = calculate_differences(df) #untuk mendapatkan selisih

#untuk menampilkan dataframe
with st.expander('View Raw Data'):
    st.dataframe(df)

#untuk mencari metrik data terakhir
month, followers, subs, refs = get_latest_monthly_metrics(df)
st.write(f'### Blog Stats for {month}')

#untuk menampilkan metrik
col1, col2, col3 = st.columns(3)
col1.metric('Followers', followers[0], delta=round(followers[1])) #metrik follower
col2.metric('Email Subscribers', subs[0], delta=round(subs[1])) #metrik subscriber
col3.metric('Referred Members', refs[0], delta=round(refs[1])) #metrik member


#untuk menampilkan grafik
#grafik pertama
fig_followers = px.line(df, x=df.date, y='followers', title='Followers')
st.plotly_chart(fig_followers, use_container_width=True)
#grafik pertama

#grafik kedua
plot_col1, plot_col2 = st.columns(2)

fig_subscribers = px.bar(df, x=df.date, y='email_subs', title='Email Subscribers')
plot_col1.plotly_chart(fig_subscribers, use_container_width=True)

fig_subscribers = px.bar(df, x=df.date, y='referred_members', title='Referred Members')
plot_col2.plotly_chart(fig_subscribers, use_container_width=True)
#grafik kedua
#Akhir halaman utama