

function encode(e){return e.replace(/[^]/g,function(e){return"&#"+e.charCodeAt(0)+";"})}
function htmlDecode(input) {
    var doc = new DOMParser().parseFromString(input, "text/html");
    return doc.documentElement.textContent;
}
// // Highlight code
shiki.getHighlighter({
    theme: 'nord'
})
.then(highlighter => {
    $(".b-code").each( function () {
        var code = highlighter.codeToHtml(removeExtraIndentation($(this).text()), { lang: $(this).attr("data-lang") });
        // var code = highlighter.codeToHtml($(this).text(), { lang: $(this).attr("data-lang") });
        this.innerHTML = code;
    });
})
var link_no = 1;
$(".p-link").each(function () {
    $(this).attr("id", "link-"+link_no);
    $("#links").append(`<li>- <a href="#link-${link_no}" class="underline">${$(this).text()}</a></li>`);
    link_no += 1;
})

var sidenav_static = false;
$(window).on('scroll', function() {
    if (($(window).scrollTop() >= $('.sidenav').offset().top + $('.sidenav').outerHeight() - window.innerHeight) && (!sidenav_static)) {
        $(".sidenav").css("position", "sticky");
        $(".sidenav").css("top", "-"+($('.sidenav').outerHeight() - window.innerHeight)+"px");
        sidenav_static = true
    }
});

// document.querySelectorAll('div.b-code').forEach(el => {
//     // then highlight each
//     $(el).text = removeExtraIndentation($(el).text());
//     hljs.highlightElement(el);
//   });