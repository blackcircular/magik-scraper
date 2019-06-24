## magik-scraper
ดึงข้อมูลของกองทุนรวมมาเก็บไว้ในไฟล์ CSV (ข้อมูลอัพเดทล่าสุดตามเว็บไซต์ WealthMagik)

## Features
* NAV ล่าสุด
* ค่าการเปลี่ยนแปลงของ NAV
* ราคารับซื้อคืน
* ราคาขาย
* ข้อมูล ณ วันที่

## Requirement
* Python 3.6+
* Requests 2.22.0
* Beautiful Soup 4.7.1

## Download
Clone หรือ Download as zip

## Quickstart
```python
# url from Fund Performance not a Fund Profile!
url = 'https://www.wealthmagik.com/FundInfo/FundPerformance-TMBAM-MIXBAL-TMBAALF-กองทุนเปิดทหารไทยจัดทัพลงทุน%20ระยะยาว'
filename = 'TMBAALF'
main(url, filename)
