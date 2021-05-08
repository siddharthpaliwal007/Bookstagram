import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';
import { Row, Col, Container } from "reactstrap";
// import "bootstrap/dist/css/bootstrap.css";
// import "font-awesome/css/font-awesome.min.css";
import { withRouter } from 'react-router';



import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';
import img1 from '../../assets/images/img1.png';
import img2 from '../../assets/images/img2.png';
import img3 from '../../assets/images/img3.png';
import img4 from '../../assets/images/img4.png';
import img5 from '../../assets/images/img5.png';
import img6 from '../../assets/images/img6.png';
import img7 from '../../assets/images/img7.png';
import img8 from '../../assets/images/img8.png';
import img9 from '../../assets/images/star_red.png';
import img10 from '../../assets/images/star_black.png';
import img11 from '../../assets/images/cd_icon.png';
import img12 from '../../assets/images/audio_icon.png';
import img13 from '../../assets/images/upcoming_event_icon.png';
const BookList = props => {

    const [data, setData] = useState([]);
    const [errValue, setErrValue] = useState();

    useEffect(() => {
        getAllBooks();
    }, []);

    const getAllBooks = () => {
        axiosMain
            .get('/book/')
            .then(response => {
                if (response.status === 200) {
                    console.log("Response", response.data)
                    setData(response.data);
                    toast.success(`User Books Fetch Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                }
            })
            .catch(error => {
                setErrValue(error);
                console.error('Error', error);
                setErrValue("This Books Fetch Failed")
            });
    };

    const handleSelect = (id) => {
        props.history.push({
            pathname: `/book-description`,
            state: {
                bookId: id,
            },
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


            <Container>
                <div className="content ">
                    <Row>
                        <Col xs="4">
                            <div className="music_box ">
                                <img src={img11} className="float_l" />
                                <h2 className="music_box_h2">AUDIO PODCASTS</h2>
                                <p className="desc float_l ">Bookstagram lauches new experiance with audio blogging and story podcasts</p>
                            </div>
                        </Col>
                        <Col xs="4">
                            <div className="music_box">
                                <img src={img12} className="" />
                                <h2 className="music_box_h2">LISTEN BEFORE PURCHASE</h2>
                                <p className="desc ">Listen to the previews before you buy</p>
                            </div>
                        </Col>
                        <Col xs="4">
                            <div className="music_box ">
                                <img src={img13} className="" />
                                <h2 className="music_box_h2">AUTHOR SCREENS</h2>
                                <p className="desc ">Launching on 5th April 2021,Author's insightful and interactive user experience</p>
                            </div>
                        </Col>

                    </Row>

                </div>
            </Container>

            <Container>
                <div className="maincontent ">
                    <Row>

                        <h3>LATEST ARRIVALS IN BOOKSTAGRAM
                <div className="arrow">
                            </div></h3>
                        {data.length >= 1 && data.map(({ id, name, desc, dp, rate, authJSON }, index) => (
                            <Col xs="3">
                                <div className="box1 " onClick={() => handleSelect(id)}>
                                    <div className="arrival_img"><div className="arrival_imgcard" ><img src={dp} width="226" height="228" /></div></div>
                                    <h4>&nbsp;&nbsp;&nbsp;&nbsp;<a >{name}</a> &nbsp;&nbsp;<i><small><a href="#">by {authJSON.first_name}</a></small></i></h4>
                                    <p><b>{name}</b> {desc}</p>
                                    <p>$ {rate}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="Mens-Product-Detail-Page.html">ADD TO CART</a></p>
                                </div>
                            </Col>
                        ))}
                    </Row>
                </div>
            </Container>
        </React.Fragment >
    );
}

export default withRouter(BookList);        