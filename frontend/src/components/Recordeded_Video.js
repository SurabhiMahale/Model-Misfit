// import { useState } from "react";
// const Video=()=>{
//   const [vid,setVid]=useState(null)

//   const handelChange=(event)=>{
//     setVid(URL.createObjectURL(event.target.files[0]))

//   }
//   return(
//     <>
    
//     <input type="file" accept=".mp4,.mkv" onChange={handelChange}/>
//     <iframe src={vid}></iframe>
//     </>
//   )
// }
// export default Video;


// import { useState } from "react";

// const Video = () => {
//   const [vid, setVid] = useState(null);

//   const handleChange = (event) => {
//     setVid(URL.createObjectURL(event.target.files[0]));
//   };

//   return (
//     <>

//     <>
//     <label htmlFor="file-upload" className="custom-file-upload">
//         Choose a video file
//       </label>
//       <input id="file-upload" type="file" accept=".mp4,.mkv" onChange={handleChange} style={{ display: "none" }} />
//       <div style={{
//         width: "90%", // Adjust the width of the video container
//         maxWidth: "1000px", // Set a maximum width for larger screens
//         margin: "0 auto", // Center the video container horizontally
//       }}>
//         <iframe
//           src={vid}
//           style={{
//             width: "800px", // Make the iframe take the full width of its container
//             height: "600px", // Set the height of the video screen to 400px
//             border: "none", // Remove the border of the iframe
//           }}
//         />
//       </div>
//     </>
//      </>
//   );
// };

// export default Video;

import { useState } from "react";

const Video = () => {
  const [vid, setVid] = useState(null);

  const handleChange = (event) => {
    setVid(URL.createObjectURL(event.target.files[0]));
  };

  return (
    <div style={{
      // margin:"5%",
      
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      height: "700px",
      width:"1000px",
      backgroundColor: "#f0f0f0",
    }}>
      <label htmlFor="file-upload" className="custom-file-upload">
        Choose a video file
      </label>
      <input id="file-upload" type="file" accept=".mp4,.mkv" onChange={handleChange} style={{ display: "none" }} />
      <div style={{
        width: "70%",
        maxWidth: "800px",
        backgroundColor: "transparent",
        textAlign: "center",
        marginTop: "20px",
      }}>
        <iframe
          src={vid}
          style={{
            width: "100%",
            height: "70vh",
            border: "none",
          }}
        />
      </div>
    </div>
  );
};

export default Video;
