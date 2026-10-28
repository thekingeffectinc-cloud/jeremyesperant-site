// Service-area map: Leaflet + OpenStreetMap tiles (no API key). Counties from js/counties.js.
(function(){
  var el=document.getElementById('service-map');
  if(!el)return;
  if(typeof L==='undefined'){el.innerHTML='<p class="map-fallback">Map could not load. United Realty Group Inc., 7300 W. McNab Road, Suite 119, Tamarac, FL 33321 — serving Broward &amp; Palm Beach counties.</p>';return;}
  var office=[26.2083,-80.2784]; // 7300 W. McNab Rd, Tamarac, FL 33321 (approx.)
  var map=L.map(el,{scrollWheelZoom:false}).setView(office,9);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'&copy; OpenStreetMap contributors'}).addTo(map);
  var styles={'Broward County':{color:'#0d4f4f',fillColor:'#0d4f4f',fillOpacity:.22,weight:2},'Palm Beach County':{color:'#ad8c42',fillColor:'#c4a35a',fillOpacity:.25,weight:2}};
  if(window.SERVICE_COUNTIES){
    var layer=L.geoJSON(window.SERVICE_COUNTIES,{style:function(f){return styles[f.properties.name]},onEachFeature:function(f,l){l.bindTooltip(f.properties.name,{sticky:true})}}).addTo(map);
    map.fitBounds(layer.getBounds(),{padding:[10,10]});
    map.setView(office,map.getZoom()); // keep the office at center
  }
  L.circleMarker(office,{radius:9,color:'#fff',weight:3,fillColor:'#c0392b',fillOpacity:1}).addTo(map)
   .bindPopup('<strong>Jeremy Esperant</strong><br>Sales Associate | United Realty Group Inc.<br>7300 W. McNab Road, Suite 119<br>Tamarac, FL 33321<br><a href="tel:+19546434239">954-643-4239</a>').openPopup();
})();
