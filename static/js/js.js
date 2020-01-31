//rand = function(min,max){
//  return Math.floor(Math.random()*(max-min+1))+min;};
//
//$(function(){
//  $('.markdownx-preview').insertAfter('.markdownx');
//});
//
//$(function(){
//$('.markdownx-preview, .markdownx').wrapAll('<div class="editor_main"></div>');
//});
//
//$(function(){
//$('label[for="id_tag"], select').wrapAll('<div class="editor_tag"></div>');
//});
//
//$(function(){
//  $('.editor_tag').insertAfter('.markdownx-preview');
//});
//
//$(function () {
//  $('.markdownx-preview p').replaceWith('<textarea></textarea>');
//});
//
//
//

////メインメニューのコンテンツ部分の高さを確保、+100はヘッダーとコンテンツの間に空けている余白部分
//$(function(){
//    var biggestHeight = "0";
//    $("#main_wrap *").each(function(){
//        if ($(this).height() > biggestHeight ) {
//            biggestHeight = $(this).height()
//        }
//    });
//    $("#main_wrap").height(biggestHeight+100);
//})

//positionのabsolute指定で親要素の高さが潰れてしまったときの対処法。
$(function(){
    var biggestHeight = "0";
    $(".markdownx *").each(function(){
        if ($(this).height() > biggestHeight ) {
            biggestHeight = $(this).height()
        }
    });
    $(".markdownx").height(biggestHeight);
})



//親要素の指定()
ccc=$('label[for="id_title"]').parent('p')

aaa=$('label[for="id_tag"]').parent('p')

bbb=$('label[for="id_text"]').parent('p')

ddd=$('label[for="id_photo"]').parent('p')

//指定要素の上に移動
$(function(){
  $(aaa).insertBefore(bbb);
});

$(function(){
  $(ddd).insertBefore(bbb);
});
//$(function(){
//  $(aaa).insertBefore(bbb);
//});

//
$(function(){
document.querySelector('label[for="id_title"]').remove();
});
//element.parentNode.removeChild(element);
//document.querySelector('div.markdown-body > div.toc').removeChild(toc);

//親要素cssの適用
//$(function() {
//$('label[for="id_tag"]').parent('p').css({position:"absolute"});
//});

//$(function(){
//  $('img').click(function() {
//
//    var num = rand(1,3);
//
//    var filename = '/static/photo/header_image'+ num +'.jpg';
//
//    $('img.header_img').attr('src', filename)
//    });
//});
