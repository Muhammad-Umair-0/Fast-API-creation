import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("Iris.csv")


print(df.head())

print("shape\n",df.shape)

x = df.drop(['Id','Species'], axis=1)
y = df['Species']

print("only features\n", x)
print(x.shape)

print("\n Label \n",y)

x_train,x_test, y_train,y_test  = train_test_split(x,y,test_size=0.2)

print("train_featre")


