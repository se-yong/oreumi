$(document).ready(function(){
    $('#changeTextBtn').click(function(){
        $('#myHeading').text('안녕하세요, 강의페이지입니다!');
    });
    $('#changeColorBtn').click(function(){
        $('#myHeading').css('color', 'skyblue');
    });
    $('#addClassBtn').click(function(){
        $('#myHeading').addClass('highlight');
        $('.highlight').css('color', 'yellow');
    });
    $('#removeClassBtn').click(function(){
        $('#myHeading').removeClass('highlight');
    });
    $('#hideBtn').click(function(){
        $('#myHeading').hide();
    });
    $('#showBtn').click(function(){
        $('#myHeading').show();
    });

});