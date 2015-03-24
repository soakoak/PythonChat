function now (milliseconds) {
	var now = new Date(milliseconds);
	//now.setUTCMilliseconds(milliseconds);
	//now = new Date();
	
	return now.toLocaleString();
}

function hoursMinutes() {
	var now = new Date();
	
	if (now.getHours() < 10)
		var str = "0" + now.getHours();
	else
		var str = now.getHours();
	
	str += ":";
	
	if (now.getMinutes() < 10)
		str += "0" + now.getMinutes();
	else
		str += now.getMinutes();
	
	return str;
}