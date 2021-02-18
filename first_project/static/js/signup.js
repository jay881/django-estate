function hideSellerInfo(b){
  console.log(b)
  if(b){
    document.getElementById('seller').className = "sellerSec"
  }
  else{
    document.getElementById('seller').className = ""
  }
}
