

var a =[]
n=prompt("enter the num")
if (n > 0){
if (n == 1){
    alert(0)
}
else if (n == 2){
    a.push(0 , 1)
    alert(a)
}
else {
     a.push(0 , 1)
    while (n > a.length ) {
         num=  + a[(a.length)-2]
         a.push(num)
    }
    alert(a)
}    
}  
else{
    alert("you most enter positve number")
}

    



