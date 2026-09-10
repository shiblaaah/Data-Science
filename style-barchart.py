import plotly.express as px

data = {
        "fruits":["apples", "orange", "bananas","apples", "orange", "bananas"],
        "amount":[4,1,2,2,4,5],
        "city":["SF","SF","SF","montreal","montreal","montreal"]
        }

fig =px.bar(
        data,
        x="fruits",
        y="amount",
        color="city",
        barmode="group",
        title="fruit consumption by city"
        )

fig.update_layout(template="plotly_dark")

fig.show()

