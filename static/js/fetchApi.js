


async function getLahan(){
    let url = "http://127.0.0.1:8000/api/lahan/";
    try {
     let res = await fetch(url);
     return await res.json();
    }catch (error){
    console.log(error);
   }
  }


  async function viewLahan(){
    let lahan = await getLahan();
    console.log(lahan);
    lahan.forEach(sawah => {
      kmz.load(sawah.nama_file);
      console.log(sawah.nama_file);
     
    });
    // location.reload();
  }

  async function getPupuk(){
    let urlPupuk = "http://127.0.0.1:8000/api/pupuk/";
    try { 
      let  resp = await fetch(urlPupuk);
      return await resp.json();}
      catch(error){
        console.log(error);
      }
    }

  async function viewPupuk(){
    let pupuk =  await getPupuk();
    console.log(pupuk);
    pupuk.forEach(tempat => {
      console.log(tempat.Latitude);
      console.log(tempat.Longitude);
       L.marker([tempat.Latitude,tempat.Longitude]).addTo(map)
      .bindPopup("<b>" + tempat.nama_toko + "</b><br />" + tempat.no_tlp).openPopup();
      
    });
  }
 

  