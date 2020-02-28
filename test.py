import pandas as pd

def writeTOExcel(inputFrame):
        print("In Function")
        frame=pd.DataFrame(inputFrame,columns=['ACCOUNT_ID','ACCOUNT_NAME','ERROR MESSAGE'])
        with pd.ExcelWriter('file.xlsx') as writer:
                frame.to_excel(writer,sheet_name="Error_File",index=False)

if __name__ == "__main__":
        df=pd.read_csv("files/Account_Details_0.csv")

        insertDetails=df[['ACCOUNT_ID','ACCOUNT_NAME']] [df['MODE'] =='I']
        print(type(insertDetails))
        rowlist=[]
        for i,row in insertDetails.iterrows():
                
        writeTOExcel(rowlist)