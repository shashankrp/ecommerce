var hostname = "http://127.0.0.1:9999";
var socialAllow = ['facebook', 'instagram','twitter']
var socialLinks = {
    facebook: 'https://facebook.com', 
    instagram: "https://instagram.com", 
    twitter: "https://twitter.com",
}

function checkClick(endpoint){
    path = window.location.href
    path1 = path.split("/")
    if(endpoint == "About"){
        if(!path1.includes("about")){
            console.log("Of you could change")
            path = path + "about/"
            console.log("getting the path: "+path)
            window.location.href = path
        }
    }else{
        console.log("Other")
    }
}

function navBar(endpoint){
    path = window.location.href
    path1 = path.split("/")
    if(endpoint == "Cart"){
        if(path1.includes(endpoint)){
            path = path + "cart/"
            window.location.href = path
        }else{
            window.location.href = hostname+"/home/cart/"
        }
    }else if(endpoint == "Return"){
        if(!path1.includes(endpoint)){
            path = path + "return/"
            window.location.href = path
        }
    }else if(endpoint == "Signup"){
        if(path1.includes('signin')){
            path = path.replace("signin/","")
            path = path + "signup/"
            window.location.href = path
        }else if(path1.includes('cart')) {
            path = path.replace("cart/","")
            path = path + "signup/"
            window.location.href = path
        }else if(path1.includes('login')){
            path = path.replace("login/","")
            path = path + "signup/"
            window.location.href = path
        }else{
            console.log(path1)
            path = path + "signup/"
            window.location.href = path
        }
    }
    else if(endpoint == "SignIn"){
        if(path1.includes('signup')){
            path = path.replace("signup/","")
            path = path + "signin/"
            window.location.href = path
        }else if(path1.includes('login')){
            path = path.replace("login/","")
            path = path + "signin/"
            window.location.href = path
        }else{
            path = path + "signin/"
            window.location.href = path
        }
    }
}

function goHome(){
    window.location.href = hostname+"/home/"
}

function productSelection(productId){
    console.log(productId);
    window.location.href = hostname+"/home/productsList/?id="+productId
}

function subProd(productName){
    console.log(productName)
    window.location.href= hostname+"/home/SubproductsList/?id="+productName
}

function subsubProd(productName){
    window.location.href= hostname+"/home/SubproductsCat/?id="+productName
}





/* Social media information */
function social(media){
    if(socialAllow.includes(media)){
        window.open(socialLinks[media], "_blank")
    }
}