import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';
import profileImage from '../../assets/images/profile/2.png';
import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';
import { Row, Col, Container } from "reactstrap";
import img1 from '../../assets/images/profile/3.png';
import img2 from '../../assets/images/img8.png';
import CustomDropdown from "../../components/CustomDropdown/CustomDropdown";
import apj from "../../assets/images/apache-basics.jpg"
import { SignalCellularNullTwoTone } from '@material-ui/icons';
function shoot() {
  alert("Your book has been added to cart");
}

const Home = () => {
  const userData = JSON.parse(localStorage.getItem('userData'));

  const [category, setCategory] = useState();
  const [bookTitle, setBookTitle] = useState();
  const [description, setDescription] = useState();
  const [dp, setDp] = useState();
  const [pdf, setPdf] = useState();
  const [bookUploaded, setBookUploaded] = useState(false);

  const [errValue, setErrValue] = useState(null);
  const dispatch = useDispatch();

  const data = useSelector(state => state);

  useEffect(() => {

  }, []);

  const onImageChange = (event) => {
    if (event.target.files && event.target.files[0]) {
        let reader = new FileReader();
        reader.onload = (e) => {
            setDp(e.target.result);
        };
        reader.readAsDataURL(event.target.files[0]);
    }
}

const onPDFChange = (event) => {
  console.log("Here", event.target.files[0]);
  setPdf(event.target.files[0].webkitRelativePath)
  
}
  const addBookHandler = (e) => {
    e.preventDefault();

    const userId = localStorage.getItem('userId');
    console.log("ID:",userId)
    axiosMain
        .post('/book/', {
            name: bookTitle,
            desc: description,
            dp: dp,
            authname: userId,
            booktype: "Textual"
          })
          .then(response => {
            if (response.status === 200) {
              console.log("Response:", response.data);
              setBookUploaded(true);
            }
          })
          .catch(error => {
            console.error('Error', error);
            setErrValue("This User Book upload Failed")
          });
  }

  return (
    <React.Fragment>
      <Header />
      <Sidebar />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />

      <div className="content-body">

        <div className="container">
          <div className="row">
            <Container>
              <div className="container">
                <h2>Upload your Book</h2>
              </div>
              <br/>            
              <div className="container">

              {bookUploaded?
              <h2>Your Book was uploaded</h2>: null
                }
              {errValue?
              <h2>Your Book Failed to upload because: {errValue}</h2>: null
                }

              <input
                  className="uploadbooktextbox"
                  type="text"
                  placeholder="Category"
                  name="Category"
                  onChange={(e) => { setCategory(e.target.value) }}
                  required
                />
                <input
                  className="uploadbooktextbox"
                  type="text"
                  placeholder="BookTitle"
                  name="BookTitle"
                  onChange={(e) => { setBookTitle(e.target.value) }}
                  required
                />
                <input
                  className="reviewtext"
                  type="text"
                  placeholder="Description/Summary"
                  name="Description/Summary"
                  onChange={(e) => { setDescription(e.target.value) }}
                  required
                />
              </div>
              <div className="col-xxl-12">
              <div className="form-file">
              <input
                  type="file"
                  className="form-file-input"
                  id="customFile"
                  onChange={(e) => { onImageChange(e) }}
              />
                <label className="form-file-label" for="customFile">
                    <span className="form-file-text">Choose Cover Photo</span>
                    <span className="form-file-button">Browse</span>
                </label>
              </div>
              </div>
              <div className="col-xxl-12">
              <div className="form-file">
              <input
                  type="file"
                  className="form-file-input"
                  id="customFile"
                  onChange={(e) => { onPDFChange(e) }}
              />
                <label className="form-file-label" for="customFile">
                    <span className="form-file-text">Choose PDF File</span>
                    <span className="form-file-button">Browse</span>
                </label>
              </div>
              </div>
              <br/>            
              <button 
              className="reviewsubmit"
              onClick = {(e) => {addBookHandler(e)}}
              >
                  Upload!
                </button>
            </Container>
          </div>
        </div>
      </div>
    </React.Fragment >
  );
};

export default Home;
