#!"C:\Strawberry\perl\bin\perl.exe" -w
#print "Content-Type: text/html\n\n";


use strict;
use warnings;



print <<EOF;

<!DOCTYPE html>
<html lang="en">

<head>
  <title>Email Directory</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Boostrap CSS CDN -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  
  <!-- jQuery CDN -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <!-- Boostrap js CDN -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  

<style type="text/css">
		body {
			background-color: white;
			font-family: "Helvetica Neue", Helvetica, Arial,"微軟正黑體", sans-serif;
		}

		h1 {
			color: black;
			text-align: center;
		}

		p {
			font-family: verdana;
			font-size: 16px;
		}
	
		table {
			  border-collapse: collapse;
			  width: 100%;
			  font-size: 16px;
			}

		th, td {
			  text-align: left;
			  padding: 8px;
			}
		
		tr:nth-child(even) {
		   background-color: #f2f2f2;
		   
		 }
		
</style>

<script>

\$(document).ready(function(){

	
/*======================//
// open page load data  //
//======================*/

ReloadFunction();	

/*=============================================//
//	            Reload 刷新                    //
//=============================================*/
	\$("#reload").click(function(){
		console.log("=====>  reload");

		
		\$("#list_body").empty();
		console.log("=====>  \$('table_list tr').remove()");

		ReloadFunction();

	});

/*=====================================================//
// New Add ajax (新增 with ajax)                      //
//====================================================*/
	\$("#Add_ajax").click(function(){	
			console.log("add~~");
		\$('#resAdd').html(  "<div class='container'>"
							+	"<form autocomplete='off'>" 
							+	"<div class='form-group'>"
							+	  "<label for='user'>名稱:</label>"
							+	  "<input type='user' class='form-control' id='user' placeholder='請輸入名稱' name='user' style='width:50%'>"
							+	  "<label for='name'>姓名:</label>"
							+	  "<input type='name' class='form-control' id='name' placeholder='請輸入姓名' name='name' style='width:50%'>"
							+	  "<label for='email'>電子郵件:</label>"
							+	  "<input type='email' class='form-control' id='email' placeholder='請輸入email' name='email' style='width:50%'>"
							+	  "<label for='phone'>聯絡電話:</label>"
							+	  "<input type='phone' class='form-control' id='phone' placeholder='請輸入電話' name='phone' style='width:50%'>"
							+	"</div>"
							+	"</form>"
							+   "</div>"
							);
//		\$('#resAdd').load("./function/Add_user_ajax.pl");   // from 也可另外寫成一個html 用.load()的去呈現
		\$('#resAdd_button').html('<button id="add_submit"   class="btn_submit btn btn-info">確定</button>   <button id="cancel"   class="btn_submit btn btn-info">關閉</button>');
//      console.log("=====>  Add_ajax");
//-----------------------------------------------------------
// (1)cancle add				
			\$("#cancel").click(function(){	
				\$('#resAdd').hide().toggle();
				\$('#resAdd_button').hide().toggle();
				\$('#resAdd').html("<h1></h1><h1></h1><h1></h1>");
				\$('#resAdd_button').html("<h1></h1><h1></h1><h1></h1>");
			});
//------------------------------------------------------------			
//  (2)Submit 新增資料			
			\$("#add_submit").click(function(){					
				
				// character 
				add_user = \$("#user").val();
				add_name = \$("#name").val();
				add_email = \$("#email").val();
				add_phone = \$("#phone").val();
				
				
				
				// character escape for persent
				es_add_user = escapeHtml(\$("#user").val());
				es_add_name = escapeHtml(\$("#name").val());
				es_add_email = escapeHtml(\$("#email").val());
				es_add_phone = escapeHtml(\$("#phone").val());
				
				var add={        // get input
					  user: add_user,
					  name: add_name,
					  email: add_email,
					  phone: add_phone
					};
					console.log(add);
					
				
					
					
//				\$('#respAjax').html("This came from AJAX "+dt.user+", email="+dt.email);       
				\$.ajax({
						url: "Adduser_DB_INSERT.pl",  // insert DB Adduser_DB_INSERT.pl
						type: "POST",
						data: add,
						dataType: "json",
						error:function(XMLHttpRequest, textStatus, errorThrown) { // script call was *not* successful
/*							 \$('#respAdd_ajax').text("[responseText]: " + XMLHttpRequest.responseText 
																	   + ", [textStatus]: " + textStatus 
																	   + ", [errorThrown]: " + errorThrown);
*/
								},
								
						success: function(add_data){
								console.log("this is: success");
								
								
							
								
								console.log("[add_data] : " +add_data + ", success 沒有抓到東西")
							
/*									alert("[user]: " + es_add_user 
										+ "  ,[name]: " + es_add_user
									  + "  ,[email]: " + es_add_user
									  + "  ,[phone]: " + es_add_user);
*/									
									\$('#resSearch').html("<h3>[New Add]<h3>"
														+"<p>[user]: " + es_add_user 
														+ "<br>[name]: " + es_add_name
													  + "<br>[email]: " + es_add_email
													  + "<br>[phone]: " + es_add_phone
														+"<br><button onclick='cleanFunction()'  class='btn_submit btn btn-default'>clean</button></p>");
														
												
									// add list on page without reload
									\$("#list_body").append("<tr><td>"+ i +"</td>" 
													+   "<td>" + es_add_user + "</td>" 
													+   "<td>" + es_add_name + "</td>" 
													+   "<td>" + es_add_email + "</td>" 
													+   "<td>" + es_add_phone + "</td>"
													+ 	"<td><button id='Edit_"+ id_i + "' class='btn_submit btn btn-success data_edit'>編輯</button>" 
													+ 	"	<button id='Delect_" + id_i + "' class='btn_submit btn btn-danger date_delete'>刪除</button>"
													+	"</td></tr>");
								
									i ++;
									delete dt;
									//location.reload();
								
								
						} //--->success
						
					//
				});
				\$('#resAdd').hide().toggle();
				\$('#resAdd_button').hide().toggle();
				\$('#resAdd').html("<h1></h1><h1></h1><h1></h1>");
				\$('#resAdd_button').html("<h1></h1><h1></h1><h1></h1>");
			
			});  //--> \$("#add_submit")
	});	 //  ---> \$("#Add_ajax")	

//===============================================================================
//	Search
//===============================================================================
	\$("#Search").click(function(){
		console.log("=====> start search :");

		search_input=\$("#gsearch").val();
		//search_ce = escapeHtml(search_input);
		var search_key_word={        // get input
			  name: search_input
			};
//			console.log("get value :" + search_input);
			//console.log("get value_ec :" + search_ce);
							 	
	    \$.ajax({
				url: "DB_search_user.pl", //  search use in DB_search_user.pl
				type: "POST",
				data: search_key_word,
				dataType: "json",
				error:function(XMLHttpRequest, textStatus, errorThrown) { // script call was *not* successful
					 \$('#resSearch').text("responseText: " + XMLHttpRequest.responseText 
															   + ", textStatus: " + textStatus 
															   + ", errorThrown: " + errorThrown);
						},
				success: function(Search_result){	
												
						// if name was not found in DB 
						if(Search_result.namePERL === null ){
							//console.log(Search_result.namePERL);
							\$('#resSearch').html("<p>Sorry, can't find ["+ search_input +"]<br>Please check user name.</p>"
												+ "<button onclick='cleanFunction()'  class='btn_submit btn btn-default'>clean</button>");

						}
						else
						{							
/*								console.log("Get search result，still not replace : ");
							console.log("  [user]:  " + Search_result.userPERL
										+"  [name]:  " + Search_result.namePERL
										+"  [email]:  " + Search_result.emailPERL
										+"  [phone]:  " + Search_result.phonePERL);
*/											
						// regex : to replace & character escape
							 hit_user = Search_result.userPERL;
							 hit_user = hit_user.replace(/\"/gi, '');
							 hit_user = escapeHtml(hit_user);
							 hit_name = Search_result.namePERL;
							 hit_name = hit_name.replace(/\"/gi, '');
							 hit_name = escapeHtml(hit_name);
							 hit_email = Search_result.emailPERL;
							 hit_email = hit_email.replace(/\"/gi, '');
							 hit_email = escapeHtml(hit_email);
							 hit_phone = Search_result.phonePERL;
							 hit_phone = hit_phone.replace(/\"/gi, '');
							 hit_phone = escapeHtml(hit_phone);
							
							 hit_result={        // get value from search result 
								  user: hit_user,
								  name: hit_name,
								  email: hit_email,
								  phone: hit_phone
								};
							// check search　result	
							 console.log("Afte regex  [hit_result] ");
							 console.log("  [user]:  " + hit_user
										+"  [name]:  " + hit_name
										+"  [email]:  " + hit_email
										+"  [phone]:  " + hit_phone);

					//		\$('#resSearch01').text("responseText: " + XMLHttpRequest.responseText );
							
							\$('#resSearch').html(	"<table id='test' style='width:100%'>"
													+	"<thead>"
													+		"<tr>"
													+			"<th>User</th>"
													+			"<th>Name</th>"
													+			"<th>Email</th>"
													+			"<th>Phone</th>"
													+		    "<th>close</th>"   
													+		"</tr>"
													+	"</thead>"
													+	"<tbody>"
													+	"<tr>"
													+   	"<td>" + hit_user + "</td>" 
													+   	"<td>" + hit_name + "</td>" 
													+   	"<td>" + hit_email + "</td>" 
													+   	"<td>" + hit_phone + "</td>"
											// search 之後可以直接更改予刪除搜尋到的結果，刪除功能 待修
												//	+   "	<button onclick='EditFunction()'   class='btn_submit btn btn-success'>編輯</button>"
												//	+		"	 <button onclick='DelFunction()'  class='btn_submit btn btn-danger'>刪除</button>"	
													+       "    <td><button onclick='cleanFunction()'  class='btn_submit btn btn-default'>clear</button>"
													+   "</td>"
													+   "</tr>"
													+	"</tbody>"
													+"</table>"
													
												);	
												
									get_again=\$("#gsearch").val();
									console.log("get_again : " + search_input);
							delete search_key_word;
							delete search_input;
							
						} // --> else
						
						
				} //--->success
		}); // ----> ajax

	// [edit] & 和 [delete bottom] 也是可以寫在 search 之後
	//  ----------------------------------------------------------				
	}); // ------> \$("#Search").click(function()


});   // ---> .ready(function()



// ###########[ Reload Part]#################
// ==========================================
//          Loading list  [edit ]
//===========================================
  function List_edit(edit_i){		
		console.log("[List_edit]");
		console.log("check edit_i: " + edit_i );
		
		var edit_user=load_data[edit_i].user;
		var edit_name=load_data[edit_i].name;
		var edit_email=load_data[edit_i].email;
		var edit_phone=load_data[edit_i].phone;
		console.log("[edit_user] : " + edit_user
				+   "[edit_name] : " + edit_name
				+   "[edit_email] : " + edit_email
				+   "[edit_phone] : " + edit_phone
					);
		var es_edit_user=escapeHtml(edit_user);
		var es_edit_name=escapeHtml(edit_name);
		var es_edit_email=escapeHtml(edit_email);
		var es_edit_phone=escapeHtml(edit_phone);
		
		console.log("es_value :" + es_edit_user + ", " + es_edit_name+ ", " +es_edit_email);
		
		\$('#resEdit').html(  "<hr><div class='container p-3 my-3 border'>"
									+	"<h3>[Edit data] </h3>"
									+	"<form autocomplete='off'>" 
									+	"<div class='form-group'>"
									+	  "<label for='user'>名稱:</label>"
									+	  "<input type='user' class='form-control' id='edit_user' placeholder='請輸入名稱' name='user' style='width:50%' value="+ es_edit_user +">"
									+	  "<label for='name'>姓名:</label>"
									+	  "<input type='name' class='form-control' id='edit_name' placeholder='請輸入姓名' name='name' style='width:50%' value="+ es_edit_name +">"
									+	  "<label for='email'>電子郵件:</label>"
									+	  "<input type='email' class='form-control' id='edit_email' placeholder='請輸入email' name='email' style='width:50%' value="+ es_edit_email +">"
									+	  "<label for='phone'>聯絡電話:</label>"
									+	  "<input type='phone' class='form-control' id='edit_phone' placeholder='請輸入電話' name='phone' style='width:50%' value="+ es_edit_phone +">"
									+	"</div>"
									+	"</form>"
									+   "</div>"
									);
		\$('#resEdit_button').html("<button onclick='EditSubmitFunction(" + edit_i + ")'   class='btn_submit btn btn-info'>確定</button>"
									+"	<button onclick='EditCancelFunction(" + edit_i +")'   class='btn_submit btn btn-info'>關閉</button>");


	
 }

// ====================================
//        Loading list [ delete ]
//=======================================
 function List_delete(delete_i){  
		console.log("[List_delete]");
		console.log("check delete_i: " +  delete_i);
		var del_user=load_data[delete_i].user;
		var del_name=load_data[delete_i].name;
		var del_email=load_data[delete_i].email;
		var del_phone=load_data[delete_i].phone;
		console.log("[del_user] : "  + del_user
				+ ", [del_name] : "  + del_name
				+ ", [del_email] : " + del_email
				+ ", [del_phone] : " + del_phone
					);
		var del_data={        // get input
			  name: del_name,
			  user: del_name,
			  email: del_email,
			  phone: del_phone
			};			
			
//			alert("Delete !!!");
			
		\$.ajax({
				url: "Deluser_DB_DELETE.pl", //  delete data 
				type: "POST",
				data: del_data,
				dataType: "text",
				
				error:function(XMLHttpRequest, textStatus, errorThrown) { // script call was *not* successful
					 console.log("[responseText]: " + XMLHttpRequest.responseText 
								+ ", [textStatus]: " + textStatus 
								+ ", [errorThrown]: " + errorThrown);
				},
				success: function(deleted_data){
						console.log("data delete : " + del_data);
				ReloadFunction();		
				} //--->success				
				//console.log("~~~data delete~~  " + hit_result);
		});	
		
		
		alert("刪除: [user] :" + del_user +", [name]: "+ del_name +", [email]: "+ del_email +", [phone]: "+ del_phone);
		//  reloaf function 待補充
 } 




/* ################[ Search ]######################
//================================================//
//    search result for Delete                   //
//===============================================
	function DelFunction() {
			console.log("=====>  Delete");			
		var del_data={        // get input
			  name: hit_result.name,
			  user: hit_result.user,
			  email: hit_result.email,
			  phone: hit_result.phone
			};
			
		console.log(">>> search result for Delete:"
				+	"[user] : " + del_data.user
				+	"[name] : " + del_data.name
				+	"[email] : " + del_data.email
				+ 	"[phone] : " + del_data.phone
					);
			
		\$.ajax({
				url: "Deluser_DB_DELETE.pl", //  delete data 
				type: "POST",
				data: del_data,
				dataType: "text",
				
				error:function(XMLHttpRequest, textStatus, errorThrown) { // script call was *not* successful
					 console.log("[responseText]: " + XMLHttpRequest.responseText 
								+ ", [textStatus]: " + textStatus 
								+ ", [errorThrown]: " + errorThrown);
				},
				success: function(delete_data){
						console.log("data delete : " + del_data);
				ReloadFunction();		
				} //--->success				
				//console.log("~~~data delete~~  " + hit_result);
		});	
		alert("刪除(del): [user] :" + hit_result.user + ", [name]: "+ hit_result.name + ", [email]: "+ hit_result.email + ", [phone]: "+ hit_result.phone);
		//  reloaf function 待補充
	}*/
/*============================================================//
//   search result fot Edit                                   // 
//============================================================
	function EditFunction() {		
		//var EditWindow = window.open("./function/Edit_user.pl", "MsgWindow", "width=700,height=600");
		
		console.log("[user]:" + hit_result.user
				+	"[name]:" + hit_result.name
				+	"[email]:" + hit_result.email
				+	"phone]:" + hit_result.phone
				);	
		
		var es_edit_user=escapeHtml(hit_result.user);
		var es_edit_name=escapeHtml(hit_result.name);
		var es_edit_email=escapeHtml(hit_result.email);
		var es_edit_phone=escapeHtml(hit_result.phone);
		
		
		\$('#resEdit').html(  "<hr><div class='container p-3 my-3 border'>"
									+	"<h3>[Edit data] </h3>"
									+	"<form autocomplete='off'>" 
									+	"<div class='form-group'>"
									+	  "<label for='user'>名稱:</label>"
									+	  "<input type='text' class='form-control' id='edit_user' placeholder='請輸入名稱' name='user' style='width:50%' value="+ es_edit_user +">"
									+	  "<label for='name'>姓名:</label>"
									+	  "<input type='text' class='form-control' id='edit_name' placeholder='請輸入姓名' name='name' style='width:50%' value="+ hit_result.name +">"
									+	  "<label for='email'>電子郵件:</label>"
									+	  "<input type='email' class='form-control' id='edit_email' placeholder='請輸入email' name='email' style='width:50%' value="+ es_edit_email +">"
									+	  "<label for='phone'>聯絡電話:</label>"
									+	  "<input type='number' class='form-control' id='edit_phone' placeholder='請輸入電話' name='phone' style='width:50%' value="+ es_edit_phone +">"
									+	"</div>"
									+	"</form>"
									+   "</div>"
									);
		\$('#resEdit_button').html("<button onclick='EditSubmitFunction()'   class='btn_submit btn btn-info'>確定</button>"
									+"	<button onclick='EditCancelFunction()'   class='btn_submit btn btn-info'>關閉</button>");
		//	\$('#resSearch').hide();
	}  */// ---> function EditFunction()
//===========================================================================
// (1)-------- search result use onclick  for cancel-------------------------	
		function EditCancelFunction() {
		
				\$('#resEdit').hide().toggle();
				\$('#resEdit_button').hide().toggle();
				\$('#resEdit').html("<h1></h1><h1></h1><h1></h1>");
				\$('#resEdit_button').html("<h1></h1><h1></h1><h1></h1>");

		}				
// (2)---------  search result  onclick  for submit  ----------------------	
		function EditSubmitFunction(edit_i) {
			
			console.log("[edit_i] : " + edit_i);
			// 取編輯後的值
					edit_user = \$("#edit_user").val();
					edit_name = \$("#edit_name").val();
					edit_email = \$("#edit_email").val();
					edit_phone = \$("#edit_phone").val();
			// character escape for front-end	persent	
			
					var es_edit_user = escapeHtml(edit_user);
					var es_edit_name = escapeHtml(edit_name);
					var es_edit_email = escapeHtml(edit_email);
					var es_edit_phone = escapeHtml(edit_phone);
					
					
//					if (edit_user === edit_ex_name){
//						edit_ex_name = edit_user;
//						es_edit_ex_name = es_edit_user;
//					}
					
					var edit_data={        // for ajax
						  user: edit_user,
						//  name: edit_name,
						  email: edit_email,
						  phone: edit_phone,
						};
		//----------------------------					
		//  check edit value					
					console.log("show get update value:");
					console.log("  [user]:  " + edit_user
								+"  [name]:  " + edit_name
								+"  [email]:  " + edit_email
								+"  [phone]:  " + edit_phone);
								
				\$.ajax({
						url: "Edituser_DB_UPdate_old.pl",  // insert DB Adduser_DB_INSERT.pl
						type: "POST",
						data: edit_data,
						dataType: "json",
						error:function(XMLHttpRequest, textStatus, errorThrown) { // script call was *not* successful
	//							 \$('#respAdd_ajax').text("[responseText]: " + XMLHttpRequest.responseText 
	//																	   + ", [textStatus]: " + textStatus 
	//																	   + ", [errorThrown]: " + errorThrown);
								 consloe.log("[responseText]: " + XMLHttpRequest.responseText 
																		   + ", [textStatus]: " + textStatus 
																		   + ", [errorThrown]: " + errorThrown);
	
								},
						success: function(edit_output){
						// if(){}else{}
								console.log("this is: success: "+ edit_output);
								//console.log("this is: success: "+ edit_output.[0]);
									console.log("[user]: " + edit_output.userPERL 
									  + "  ,[name]: " + edit_output.namePERL 
									  + "  ,[email]: " + edit_output.emailPERL 
									  + "  ,[phone]: " + edit_output.phonePERL 
									  );

								ReloadFunction();
								} //--->success
								
								
					}); // ---> ajax
						
					\$('#resAdd').hide().toggle();
					\$('#resAdd_button').hide().toggle();
					\$('#resAdd').html("<h1></h1><h1></h1><h1></h1>");
					\$('#resAdd_button').html("<h1></h1><h1></h1><h1></h1>");
	
			} //---> EditSubmitFunction()
/*==================================================//
//  搜尋結果清除                                   //
//=================================================*/
	function cleanFunction() {
		document.getElementById('gsearch').value = '';
		\$('#resSearch').empty();	
		\$('#resSearch01').empty();
		
		 //delete search_input;
	}




/*==============================//
//        escape character     //
//=============================*/
// 前端跳脫 
var entityMap = {
	  '&': '&amp;',
	  '<': '&lt;',
	  '>': '&gt;',
	  '"': '&quot;',
	  "'": '&#39;',
	  '/': '&#x2F;',
	  '`': '&#x60;',
	  '=': '&#x3D;'
	  
	};

function escapeHtml (string) {
  return String(string).replace(/[&<>"'`=\/]/g, function (s) {
    return entityMap[s];
  });
}



 //========================
//  Reload

	function ReloadFunction() { 
	console.log("=====>  reload");
	\$("#table_list tbody").empty();
    \$.ajax({
		type: "POST",
		url: "DB_SELECT_ALL.pl", // URL of the Perl script
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		error: function(XMLHttpRequest, textStatus, errorThrown) { // script call was *not* successful
		         \$('#resReload').text("responseText: " + XMLHttpRequest.responseText 
														   + ", textStatus: " + textStatus 
														   + ", errorThrown: " + errorThrown);
		        
		        console.log("ajax  fail");
				}, //  --->error 						
		success: function(data){
//				   data contains the JSON values returned by the Perl script
					console.log(data);
					load_data=data;
//				 object 起始值是 0 
					 i =1; //for counter
					\$.each(data, function(row_head, row_data){
							var data_user  = row_data.user;
							var data_email = row_data.email;
							var data_name = row_data.name;
							var data_phone = row_data.phone;
							
							var ec_data_user = escapeHtml(row_data.user);
							var ec_data_email =  escapeHtml(row_data.email);
							var ec_data_name =  escapeHtml(row_data.name);
							var ec_data_phone =  escapeHtml(row_data.phone);
//					console.log("[ec_data_user] : " + ec_data_user + " | [ec_data_name] : " + ec_data_name);
					
//                 adding second item after 1st item
					 id_i= i-1;  // object 起始值是 0 
//					\$("table tbody:nth-child(1)").after("<tr><td> Item Second </td></tr>");
//					\$("table tbody:last-child").before("<tr id='row_"+i+"'><td>"+ i +"</td>" 
					\$("#list_body").append("<tr id='row_"+i+"'><td>"+ i +"</td>" 
														+	"<td>" + ec_data_user + "</td>" 
														+ 	"<td>" + ec_data_name + "</td>" 
														+ 	"<td>" + ec_data_email + "</td>" 
														+ 	"<td>" + ec_data_phone + "</td>"	
														+ 	"<td><button onclick='List_edit("  + id_i + ")' id='Edit_"   + id_i + "' class='btn_submit btn btn-success list_edit'>編輯</button>" 
														+ 	"	 <button onclick='List_delete("+ id_i + ")' id='Delect_" + id_i + "' class='btn_submit btn btn-danger list_delete'>刪除</button>"
														+	"</td></tr>");	

						i++;
						
					});
			
				} // -->success
	
	}); // -->ajax
				
	};
	
</script>	
		
</head>

<body>

<div class="jumbotron text-center">
  <h1>[Quizz]:Email Directory</h1>
  <p>2021/07/26 ~ 2021/08/11       <a href="http://localhost/project_home.htm" class="btn btn-info" role="button">Home</a></p>
</div> 


<div class="container">
  <p>
<lu>
	<li>新增聯絡人 - 姓名、顯示名稱、行動電話、Email</li>
	 <li>透過 Ajax 新增聯絡人，並更新列表資料(不重整頁面)</li>
	 <li>透過 Ajax 編輯單筆聯絡人(不重整頁面)</li>
	 <li>刪除聯絡人</li>
	 <li>提供關鍵字查詢聯絡人功能(查姓名欄)</li>
</lu> 
	 </p>  
	 
	 <div class="form-group">
	 <h2>Email Diectory manegement</h2>
	 
<!--	// [按鈕範例 ] 
		<div class="form-group">
			  <button id="reload"   class="btn_submit btn btn-default">Reload</button> 
			  <button onclick="EditFunction()"   class="btn_submit btn btn-success">編輯</button>
			  <button id="Edit_ajax"   class="btn_submit btn btn-success">編輯 ajax</button>	  
			  <button id="Delect"   class="btn_submit btn btn-danger">刪除</button>	
			  <button onclick="AddFunction()"   class="btn_submit btn btn-primary">新增</button>
	     	<button id="Add_ajax"   class="btn_submit btn btn-primary">新增</button>
				<button onclick="ReloadFunction()" id="reload"   class="btn_submit btn btn-default">Reload</button>

		 </div>  
-->
		<div class="form-group">
			
			<button id="Add_ajax"   class="btn_submit btn btn-primary">新增</button>
			<button id="reload"   class="btn_submit btn btn-default">Reload</button>
		  <div id="resAdd" class="form-group"></div>
		  <div id="resAdd_button" class="form-group"></div>
		</div>	
	</div>
<hr>		


<!--  =====================
		Search user 
      ===================== -->	
	<h2>Search</h2>	
	<form autocomplete="off">
		
    <!-- search input -->
		<div class="form-group">
			 <label for="gsearch"></label>
			 <input type="search" class="form-control" id="gsearch" placeholder="請輸入姓名(name)" name="gsearch">	 
		</div>
	</form>	
    <!-- search botton -->
		<div class="form-group">
			 <button id="Search"   class="btn_submit btn btn-info">搜尋</button>
		</div>
	<!-- search result -->
		<div class="form-group">
			<div id="resSearch"></div> 
		
		</div>
		  <div id="resEdit" class="form-group"></div>
		  <div id="resEdit_button" class="form-group"></div>
		
<hr>
	<!-- =================== 
	       list user 
	    ===================== -->
		<div class="form-group">
		<h2>Current List<h2>  
			
			<div id="resReload"></div>		
		
			<table id='table_list' style="width:100%">
				<thead>
					<tr>
						<th>No.</th>
						<th>User</th>
						<th>Name</th>
						<th>Email</th>
						<th>Phone</th>
						<th>Edit / Delete </th>    
					</tr>
				</thead>
				<tbody id="list_body">
				</tbody>
			</table> 
			<hr>
		</div>	
</div>	

<!-- ============================================================== -->


</body>

</html>
EOF