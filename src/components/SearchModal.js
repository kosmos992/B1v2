/*global Tmapv2*/
import { useState } from "react";
import axios from "axios";
import AddressList from "./AddressList";

const SearchModal = ({ getCoords }) => {
  const [address, setAddress] = useState("");
  const onChangeAddress = (e) => setAddress(e.target.value);
  const [nameList, setNameList] = useState([]);

  const load = () => {
    if (address !== "") {
      const names = [];
      const searchKeyword = address;
      axios({
        method: "GET",
        url: "https://apis.openapi.sk.com/tmap/pois?version=1&format=json&callback=result",
        async: false,
        // axios는 get으로 파라미터 전달 시 data 대신 params를 써야
        params: {
          appKey: "l7xx2eff6322cd2944cab62446d299f7f6e3",
          searchKeyword: searchKeyword,
          resCoordType: "EPSG3857",
          reqCoordType: "WGS84GEO",
          count: 10,
        },
      }).then((response) => {
        const resultpoisData = response.data.searchPoiInfo.pois.poi;

        resultpoisData.forEach((e) => names.push(e));

        // for (const k in resultpoisData) {
        //   const noorLat = Number(resultpoisData[k].noorLat);
        //   const noorLon = Number(resultpoisData[k].noorLon);
        //   const name = resultpoisData[k].name;
        // }

        setNameList([...names]);

        // resultpoisData가 app에 전달돼야 함

        getCoords(resultpoisData);
      });
    } else setNameList([]);
  };

  return (
    <div style={{ position: "fixed", zIndex: 1 }}>
      <input
        type="text"
        id="searchKeyword"
        name="searchKeyword"
        onChange={onChangeAddress}
      ></input>
      <button id="btn_select" onClick={load}>
        검색
      </button>
      <br />
      {nameList.length === 0 ? null : <AddressList nameList={nameList} />}
    </div>
  );
};

export default SearchModal;
