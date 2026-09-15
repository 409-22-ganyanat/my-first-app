import streamlit as st
st.title("Khai Kue Chiwit (Eggs are life)")
st.divider()
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price*0.07
net_price = price-vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นางสาวกัญญาวีร์ แสนคำ เลขที่ 19 ม.4/9")
st.write("นางสาวกัญญานัท ละอำ เลขที่ 22 ม.4/9")
st.write("นางสาวณัฏฐณิชชา สัจจ์ธัมม์ เลขที่ 23 ม.4/9")
st.write("นางสาวปิโยรส แย้มเอิบสิน เลขที่ 45 ม.4/9")
