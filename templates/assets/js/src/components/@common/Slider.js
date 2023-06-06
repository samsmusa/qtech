import React from "react";

export default function Slider(props) {
  const [image, setImage] = React.useState(
    Math.floor(Math.random() * props?.data?.length)
  );
  return (
    <div className="">
      {props?.data && <img className="h-44 w-full" src={props?.data[image]} />}
    </div>
  );
}
