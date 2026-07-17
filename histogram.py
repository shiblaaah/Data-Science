import plotly.express as px
df=px.data.tips()
fig=px.histogram(df,x="total_bill",color="sex",nbins=30,marginal="rug",
        title="Distribution of Total Bills by GEnder")
fig.show()
