/* function play(sound){
if (sound == "do")
    {
        var audio = new Audio('assets/note1.wav');
        audio.play();
    }   
else if (sound == "re")
{
    var audio = new Audio('assets/note2.wav');
    audio.play();
}  
else if (sound == "mi")
{
     
    var audio = new Audio('assets/note3.wav');
    audio.play();          
}  
else if (sound == "fa")
{
    var audio = new Audio('assets/note4.wav');
    audio.play();          
}  
else if (sound == "se")
{
    var audio = new Audio('assets/note5.wav');
    audio.play();          
}  
else if (sound == "la")
{
    var audio = new Audio('assets/note6.wav');
    audio.play();           
} 
else if (sound == "si")
{
    var audio = new Audio('assets/note7.wav');
    audio.play();         
}  

} */

function play(sound){
    var audio = new Audio('assets/note'+ sound +'.wav');
    audio.play();
}


