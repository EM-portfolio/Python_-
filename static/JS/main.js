$(function() {

    //URL入力部分
    $('.show').click(function(){
        $('p.hidden').fadeToggle(1000);
    });
    // Howtosite_use
    $('.foot_useA').click(function(){
        $('#site').addClass("open").fadeIn();
    });
    $('.foot_useB').click(function(){
        $('#howtouse').addClass("open").fadeIn();
    });
    $(".close").click(function(){
        $("#site, #howtouse").removeClass("open").fadeOut();
        // イベントのハブリングを解除
        return false;
    });



    // 要修正
    // document.addEventListener("DOMContentLoaded", function() {
    //     // メッセージが既に表示されていなければ追加
    //     if (!sessionStorage.getItem("scrollMessageShown")) {
    //         const navButtons = document.getElementById("nav-buttons");
    //         const message = document.createElement("p");
    //         message.textContent = "スクロールしてください。";
    //         message.style.color = "#0e536d";
    //         message.style.fontWeight = "bold";
    //         message.style.marginTop = "10px";
    //         navButtons.insertAdjacentElement("beforebegin", message);

    //         // 表示されたことをsessionStorageに記録
    //         sessionStorage.setItem("scrollMessageShown", "true");
    //     }
    // });
    
});//end_func