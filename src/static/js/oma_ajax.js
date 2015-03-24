function loadMsgs(cUser, cChat, cDelta)
{
	var request = XMLHttpRequest();
	
	request.onreadystatechange = function(){ 
		
		if( request.readyState == 4 )
		{
			//console.log( request.responseText );
			var jsonObj = JSON.parse( request.responseText );
			
			var newMsgs = "";
			
			for (var i = 0; i < jsonObj.messages.length; i++)
			{
				newMsgs += makeMsg(
								jsonObj.messages[i].user,
								jsonObj.messages[i].chat,
								jsonObj.messages[i].message,
								jsonObj.messages[i].timestamp,
								cUser)
			}
			
			//console.log( newMsgs );
			document.getElementById("msg_list").innerHTML = newMsgs;
		}
	}
	
	var method = "GET";
	var destination = "./query";
	
	var params = [];
	
	if( cChat )
	{	
		params.push( "chat=" + cChat );
	}
	
	if( cDelta )
	{
		params.push( "delta=" + cDelta );
	}
	
	if( params.length > 0 )
	{
		destination += "?";
		for( var i = 0, tot = params.length; i < tot; i++ )
		{
			destination += params[ i ];
			if( i < tot - 1) destination += '&';
		}
	}
	
	var async = true;
	
	request.open( method, destination, async);
	
	request.send();
}

function makeMsg(user, chat, message, timestamp, cUser)
{
	var msg = '<div class="row"><div class="col-md-12"><div class="media">';
	
	if (user == cUser)
	{
		msg += '<div class="media-body round msg msg-mine">';
	}
	else
	{
		msg += '<div class="media-body round msg msg-other">';
	}
	
	msg += '<h4 class="media-heading">' + user + " (" + chat + ')</h4>';
	msg += '<div class="row">';
	msg += '<div class="col-md-6">[' + timestamp + '] ' + message;
	msg += '</div></div></div></div></div></div>';

	return msg;
}