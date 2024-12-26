import streamlit as st

import pymysql
import pandas as pd
db_config ={
    'host':'localhost',
     'user':'root',
      'password':'kasthuri67' ,
      'database':'retail_orders'
}
conn = pymysql.connect(**db_config)
cursor=conn.cursor()
print("connected")

r=st.sidebar.selectbox("SELECT THE TABS",["ABOUT","QUERY1_TO_10","QUERY10_TO_20"])
r1,r2=None,None
if r == "ABOUT":
    st.title("Hello Teammates I am :red[Nivedha]")
    st.markdown("""
    :moon:
     
    """)
    st.title("Retail orders")
    st.snow()
elif r == "QUERY1_TO_10":
        r1=st.sidebar.selectbox("SELECT THE QUERIES",["Find top 10 highest revenue generating products",
                                                "Find the top 5 cities with the highest profit margins",
                                                "Calculate the total discount given for each category",
                                                "Find the average sale price per product category",
                                                "Find the region with the highest average sale price",
                                                "Find the total profit per category",
                                                "Identify the top 3 segments with the highest quantity of orders",
                                                "Determine the average discount percentage given per region",
                                                "Find the product category with the highest total profit",
                                                 "Calculate the total revenue generated per year"])
elif r == "QUERY10_TO_20":
        r2=st.sidebar.selectbox("SELECT THE QUERIES",["Order the segment column starting like c?",
                                                "Find minimum profit based on the Sub_category limit 10",
                                                "Find maximum list_price based on sub_category ?",
                                                "find max discount based on category?",
                                                "Find maximum profit based on sub_category?",
                                                "Top 5states with Highest Discounts?",
                                                "Region Wise Quantity Analysis",
                                                "Product Categories with Low Sales",
                                                "Impact of Discounts on Profit",
                                                "Low Performing Products"])
                                                   
                                                
if r1=="Find top 10 highest revenue generating products":
        st.snow()
        cursor.execute("select sub_category,max(sales_price) as highest_revenue from df_order group by sub_category order by max(sales_price) desc limit 10;")
        data=cursor.fetchall()
        st.title(" Find top 10 highest revenue generating products")
        df=pd.DataFrame(data,columns=['sub_category','highest_revenue'])
        st.dataframe(df)
if r1=="Find the top 5 cities with the highest profit margins":
        st.snow()
        cursor.execute("select df_orders.city,avg(df_order.profit) as highest_profit from df_orders  join df_order on df_orders.order_id = df_order.order_id group by df_orders.city order by avg(df_order.profit) desc limit 5;")
        data=cursor.fetchall()
        st.title(" Find the top 5 cities with the highest profit margins")
        df=pd.DataFrame(data,columns=['city','highest_profit'])
        st.dataframe(df)
if r1=="Calculate the total discount given for each category":
        st.snow()
        cursor.execute("select df_orders.category,sum(df_order.discount) as total_discount from df_orders join df_order on df_orders.order_id=df_order.order_id group by df_orders.category;")
        data=cursor.fetchall()
        st.title(" Calculate the total discount given for each category")
        df=pd.DataFrame(data,columns=['category','total_discount'])
        st.dataframe(df)
if r1=="Find the average sale price per product category":
        st.snow()
        cursor.execute("select avg(sales_price) as avg_sale_price , sub_category from df_order group by sub_category;")
        data=cursor.fetchall()
        st.title(" Find the average sale price per product category")
        df=pd.DataFrame(data,columns=['avg_sale_price','sub_category'])
        st.dataframe(df)
    
if r1=="Find the region with the highest average sale price":
        st.snow()
        cursor.execute("select df_orders.region,avg(df_order.sales_price) as highest_avg_sales_price from df_orders join df_order on df_orders.order_id=df_order.order_id group by region order by avg(df_order.sales_price) desc limit 1;")
        data=cursor.fetchall()
        st.title(" Find the region with the highest average sale price")
        df=pd.DataFrame(data,columns=['highest_avg_sales_price','region'])
        st.dataframe(df)
if r1==" Find the total profit per category":
        st.snow()
        cursor.execute("select sum(profit) as total_profit,sub_category from df_order group by sub_category;")
        data=cursor.fetchall()
        st.title(" Find the total profit per category")
        df=pd.DataFrame(data,columns=['total_profit','sub_category'])
        st.dataframe(df)
if r1=="Identify the top 3 segments with the highest quantity of orders":
        st.snow()
        cursor.execute("select df_orders.segment ,count(quantity) as highest_quantity from df_orders join df_order on df_orders.order_id=df_order.order_id group by segment order by count(quantity) desc limit 3;")
        data=cursor.fetchall()
        st.title(" Identify the top 3 segments with the highest quantity of orders")
        df=pd.DataFrame(data,columns=['highest_quantity','segment'])
        st.dataframe(df)
if r1=="Determine the average discount percentage given per region":
        st.snow()
        cursor.execute("select df_orders.region ,avg(discount_percent) as avg_discount from df_orders join df_order on df_orders.order_id=df_order.order_id group by region order by avg(discount_percent) desc;")
        data=cursor.fetchall()
        st.title(" Determine the average discount percentage given per region")
        df=pd.DataFrame(data,columns=['segment','avg_discount'])
        st.dataframe(df)
if r1=="Find the product category with the highest total profit":
        st.snow()
        cursor.execute("select sum(profit) as total_profit,sub_category from order_guvi group by sub_category having sum(profit)>1000 order by sum(profit) desc limit 1;")
        data=cursor.fetchall()
        st.title("  Find the product category with the highest total profit")
        df=pd.DataFrame(data,columns=['total_profit','sub_category'])
        st.dataframe(df)
if r1=="Calculate the total revenue generated per year":
        st.snow()
        cursor.execute("select sum(Sales_price) as totalrevenueperyear,year(str_to_date(Order_Date,'%Y-%m-%d')) as order_year from df_orders join df_order on df_orders.order_id=df_order.order_id group by order_year;")
        data=cursor.fetchall()
        st.title(" Calculate the total revenue generated per year ")
        df=pd.DataFrame(data,columns=['totalrevenueperyear','order_year'])
        st.dataframe(df)
if r2=="Order the segment column starting like c?":
        st.snow()
        cursor.execute("Select * from df_orders where Segment like 'C%';")
        data=cursor.fetchall()
        st.title("  Order the segment column starting like c? ")
        df=pd.DataFrame(data,columns=['order_id','order_date','ship_mode','segment','country','city','state ','postal_code','region','category'])
        st.dataframe(df)
                
if r2=="Find minimum profit based on the Sub_category limit 10":
        st.snow()
        cursor.execute("Select Sub_Category,min(Profit)  as minprofit from df_order group by Sub_Category limit 10;")
        data=cursor.fetchall()
        st.title("Find minimum profit based on the Sub_category limit 10")
        df=pd.DataFrame(data,columns=['sub_category','minprofit'])
        st.dataframe(df)

if r2=="Find maximum list_price based on sub_category ?":
        st.snow()
        cursor.execute("select max(List_Price) as max_listprice,Sub_Category from df_order group by Sub_Category having max(List_Price)>5000;")
        data=cursor.fetchall()
        st.title("Find maximum list_price based on sub_category ?")
        df=pd.DataFrame(data,columns=['max_listprice','sub_category'])
        st.dataframe(df)
if r2=="find max discount based on category?":
        st.snow()
        cursor.execute("select df_orders.Category, max(df_order.Discount_Percent ) as max_discount from df_orders join df_order on df_orders.order_id=df_order.order_id group by category order by max(df_order.discount_percent) desc;")
        data=cursor.fetchall()
        st.title("find max discount based on category?")
        df=pd.DataFrame(data,columns=['category','max_discount'])
        st.dataframe(df)
if r2=="Find maximum profit based on sub_category?":
        st.snow()
        cursor.execute("Select Sub_Category,max(Profit) from df_order group by Sub_Category having max(Profit)>50;")
        data=cursor.fetchall()
        st.title("Find maximum profit based on sub_category?")
        df=pd.DataFrame(data,columns=['sub_category','max(profit)'])
        st.dataframe(df)
if r2=="Top 5states with Highest Discounts?":
        st.snow()
        cursor.execute("select df_orders.state, SUM(df_order.discount) as total_discount from df_orders join df_order on df_order.order_id = df_orders.order_id group by state order by total_discount DESC LIMIT 5;")
        data=cursor.fetchall()
        st.title("Top 5states with Highest Discounts?")
        df=pd.DataFrame(data,columns=['state','total_discount'])
        st.dataframe(df)
if r2=="Region Wise Quantity Analysis":
        st.snow()
        cursor.execute("SELECT df_orders.region, SUM(df_order.quantity) AS total_quantity FROM df_orders JOIN df_order ON df_order.order_id = df_orders.order_id GROUP BY region ORDER BY total_quantity DESC;")
        data=cursor.fetchall()
        st.title("Region Wise Quantity Analysis")
        df=pd.DataFrame(data,columns=['region','total_quantity'])
        st.dataframe(df)
if r2=="Product Categories with Low Sales":
        st.snow()
        cursor.execute("SELECT df_orders.category, SUM(df_order.sales_price * df_order.quantity) AS total_revenue FROM df_orders JOIN df_order ON df_orders.order_id = df_order.order_id GROUP BY category HAVING total_revenue < (SELECT AVG(total_revenue)  FROM ( SELECT SUM(df_order.sales_price * df_order.quantity) AS total_revenue FROM df_orders JOIN df_order ON df_order.order_id = df_orders.order_id GROUP BY category) AS category_revenue);")
        data=cursor.fetchall()
        st.title(" Product Categories with Low Sales")
        df=pd.DataFrame(data,columns=['category','total_revenue'])
        st.dataframe(df)
if r2=="Impact of Discounts on Profit":
        st.snow()
        cursor.execute("SELECT CASE WHEN discount_percent > 20 THEN 'High Discount'  WHEN discount_percent BETWEEN 10 AND 20 THEN 'Medium Discount' ELSE 'Low Discount' END AS discount_category, SUM(profit) AS total_profit,(SUM(profit) / SUM(sales_price * quantity)) * 100 AS profit_margin FROM df_order GROUP BY discount_category;")
        data=cursor.fetchall()
        st.title(" Impact of Discounts on Profit")
        df=pd.DataFrame(data,columns=['discount_category','total_profit','total_margin'])
        st.dataframe(df)
if r2=="Low Performing Products":
        st.snow()
        cursor.execute("SELECT product_id, (SUM(profit) / SUM(sales_price * quantity)) * 100 AS profit_margin FROM df_order GROUP BY product_id HAVING profit_margin < 10 ORDER BY profit_margin;")
        data=cursor.fetchall()
        st.title(" Low Performing Products")
        df=pd.DataFrame(data,columns=['product_id','profit_margin'])
        st.dataframe(df)
 
          
          
  
          
          
          

