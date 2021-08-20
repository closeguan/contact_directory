# contact_directory
quizz

# 主要有  新增、編輯、刪除、搜尋、reload 列表的功能。

# [reload] 
編輯是把 current list 重 load。
寫成一個function ReloadFunction() ，page 開啟時啟動
在html 上也做一個 bottom 可以按，
    $("#reload").click(function(){}去處發動做。
	step1. 用ajax 去執行 DB_SELECT_ALL.pl，不帶input
	step2. 抓到的結果於success data
	step3. .each() 去讀 data 並用jquery append()把資料印在html  table	
	# 因為 load 時就一起把botton 印出來，為了要辨識執行功能時候是來自哪一科按鈕
	所以在id 部分有做編碼 用 i 做變數處理，onclick功能時候也帶參數進去。
	
# [新增] 
是寫在 html 裡的 botton  ，id="Add_ajax"
功能觸發是用 jquery 去做click 的 event
	$("#Add_ajax").click(function(){}
   step1.  印出 form 表單和按鈕
   step2.  定義 關閉的按鈕  ，jquery做表單hide()
   step3.  定義 submit 的按鈕
				> 取from 的 input 值，存在 add 這個物件裡
				> 餵給ajax， success 確認db 也執行正常
				> jquery 把新增的資料用append()印在html  table
				> jquery把表單hide()
				
# [搜尋] 	 
	1.  把 search 欄位的值取出包成search_key_word 這個物件，然後用 ajax 把 input 餵給 DB_search_user.pl
	2.  ajax success 的話就判斷有沒有抓到值，去把撈得的資料印處來 
	3.做一個把搜尋結果[清除]的按鈕
			
# [編輯] 
	方法1. search 的結果編輯  EditFunction() 用 onclick 觸發，產生from 表單並帶入 search 的資料可以直接編寫。
			也包含 submit 和 關閉的按鈕
	方法2. current list 自動產生地的編輯  List_edit() 帶入 id，用 onclick 觸發，
	        產生from 表單並帶入 id那行的資料在編輯欄位。
	
	____________________________________________________
		編輯[關閉]的功能 EditCancelFunction()
		編輯[submit]的功能 EditSubmitFunction(edit_i) 欄位的值取出包成edit_data 這個物件，
			然後用 ajax 把 input 餵給  Edituser_DB_UPdate.pl ，最後刷新current list

[刪除]  
	方法1. search 的結果做[刪除] DelFunction() 	，
	       用 ajax 把 input 餵給  Deluser_DB_DELETE.pl，
		   最後刷新current list
	方法2. current list 自動產生的刪除按鈕  List_delete() 帶入 id ，
	       用 ajax 把 input 餵給  Deluser_DB_DELETE.pl， 
	       最後刷新current list
_________________________________________________				
[other issue]

# 對input 的字元跳脫
	1.讓前端不破壞頁面 => 收入的input要用來呈現的地方做跳脫，存DB 的就用原始的值，到後端在做跳脫
	2.接收到前端的資料做跳脫，是避免後端到資料庫破壞後段程式執行與 SQL 語法
	
# 後端程式執行要有 error catch 得環節	


