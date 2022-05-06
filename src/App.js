/*global Tmapv2*/

import "./App.css";
import SearchModal from "./components/SearchModal";
import { useState, useEffect } from "react";

function App() {
  const [showModal, setShowModal] = useState(false);
  const ctrlModal = () => setShowModal(!showModal);
  const [coords, setCoords] = useState([]);
  const [markerArr, setMarkerArr] = useState([]);
  const getCoords = (a) => setCoords(a);
  var positions = [];

  useEffect(() => {
    const map = new Tmapv2.Map("TMapApp", {
      center: new Tmapv2.LatLng(37.59644996896789, 127.06004762649577),
      width: "100%",
      height: "100%",
      zoom: 18,
    });

    // var marker = new Tmapv2.Marker({
    //   position: new Tmapv2.LatLng(37.566481622437934, 126.98452302169841), //Marker의 중심좌표 설정.
    //   icon: "https://tmapapi.sktelecom.com/upload/tmap/marker/pin_b_m_1.png",
    //   iconSize: new Tmapv2.Size(24, 38),
    //   // title: name,
    //   map: map, //Marker가 표시될 Map 설정..
    // });
    var marker;

    for (var k in coords) {
      var noorLat = Number(coords[k].noorLat);
      var noorLon = Number(coords[k].noorLon);
      var name = coords[k].name;

      var pointCng = new Tmapv2.Point(noorLon, noorLat);
      var projectionCng = new Tmapv2.Projection.convertEPSG3857ToWGS84GEO(
        pointCng
      );

      var lat = projectionCng._lat;
      var lon = projectionCng._lng;

      console.log(lat, lon);
      positions.push({ title: name, lonlat: new Tmapv2.LatLng(lat, lon) });

      // var marker = new Tmapv2.Marker({
      //   position: new Tmapv2.LatLng(lat, lon),
      //   icon: "https://tmapapi.sktelecom.com/upload/tmap/marker/pin_b_m_1.png",
      //   iconSize: new Tmapv2.Size(24, 38),
      //   // title: name,
      //   map: map,
      // });

      markerArr.push(marker);
    }

    for (var i = 0; i < positions.length; i++) {
      //for문을 통하여 배열 안에 있는 값을 마커 생성
      var lonlat = positions[i].lonlat;
      var title = positions[i].title;
      //Marker 객체 생성.
      marker = new Tmapv2.Marker({
        position: lonlat, //Marker의 중심좌표 설정.
        icon: "https://tmapapi.sktelecom.com/upload/tmap/marker/pin_b_m_1.png",
        iconSize: new Tmapv2.Size(24, 38),
        map: map, //Marker가 표시될 Map 설정.
        title: title, //Marker 타이틀.
      });
    }
    console.log(coords);
    console.log(positions);
  }, [coords, markerArr, positions]);

  return (
    <div className="App">
      <div>
        메인페이지
        <button onClick={ctrlModal}>"진짜주소검색"</button>
        <div
          id="TMapApp"
          style={{
            height: "100%",
            width: "100%",
            position: "fixed",
            zIndex: 0,
          }}
        />
        {showModal ? <SearchModal getCoords={getCoords} /> : null}
      </div>
    </div>
  );
}

export default App;
