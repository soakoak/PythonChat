function matchNick (nick) 
{
	var re = /^[a-z0-9 ]*$/i;
	var result = nick.match(re);
	
	return result;
}

function matchMsg (msg) 
{
	var re = /^[a-�0-9\/,:;\-_!?@#%&\{\}\[\] ]*$/i;
	var result = msg.match(re);
	
	return result;
}

function validate(form)
{
	//alert(matchMsg(form.elements["message"].value));
	var msg = form.elements["message"].value;
	//console.log("msg: " + msg);
	if( !(msg.trim() === "") && matchMsg(msg) )
		{
		//alert("L�ytyi!");
		form.submit();
		//return true;
		}
	else
		{
		//alert("Ei l�ytynyt!");
		return false;
		}
}