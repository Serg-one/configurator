var configBtns = document.getElementsByClassName('config')

for (i = 0; i < configBtns.length; i++) {
	configBtns[i].addEventListener('click', function(){
		var platformId = this.dataset.platform
		var action = this.dataset.action
		var path = this.dataset.url

		console.log('platformId:', platformId, 'Action:', action)
		post_to_url(url, {'platformId': platformId}, post )
	})
}

function post_to_url(path, params, method) {
    method = method || "post"; // Set method to post by default, if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}

// for (i = 0; i < updateBtns.length; i++) {
// 	updateBtns[i].addEventListener('click', function(){
// 		var platformId = this.dataset.platform
// 		var action = this.dataset.action
		
//         console.log('platformId:', platformId, 'Action:', action)
        
//         console.log('USER:', user)
        
//         if (user == 'AnonymousUser'){
// 			addCookieItem(productId, action)
// 		}else{
// 			updateUserOrder(productId, action)
// 		}
//     })
// }

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/configurator/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}
