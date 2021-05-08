import React, { useEffect } from 'react';
import $ from 'jquery';

const Spinner = () => {

  useEffect(() => {
    $(window).on("load", () => {
      $('#preloader').fadeOut(500);
    });
  }, []);

  return (
    <div id="preloader">
      <i>.</i>
      <i>.</i>
      <i>.</i>
    </div>
  )
}

export default Spinner;
