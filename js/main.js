(function(){
  var t=document.querySelector('.nav-toggle'),n=document.querySelector('.nav');
  if(t&&n)t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});
  var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
  // Contact forms: no backend yet — compose an email to Jeremy
  document.querySelectorAll('.js-mailto-form').forEach(function(f){
    f.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(f),b='';
      d.forEach(function(v,k){if(v)b+=k.charAt(0).toUpperCase()+k.slice(1)+': '+v+'\n'});
      location.href='mailto:'+f.dataset.to+'?subject='+encodeURIComponent(f.dataset.subject+' — JeremyEsperant.com')+'&body='+encodeURIComponent(b);});
  });
  // Listing filters
  document.querySelectorAll('.chip[data-filter]').forEach(function(c){
    c.addEventListener('click',function(){var v=c.dataset.filter;
      document.querySelectorAll('.chip').forEach(function(x){x.classList.toggle('is-active',x===c)});
      document.querySelectorAll('.js-listings .listing').forEach(function(l){l.style.display=(v==='all'||l.dataset.type===v)?'':'none'});});
  });
})();
