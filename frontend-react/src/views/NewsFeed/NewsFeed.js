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
import img1 from '../../assets/images/profile/3.png';
import img2 from '../../assets/images/img8.png';

const NewsFeed = props => {

    const [data, setData] = useState([]);
    const [errValue, setErrValue] = useState();


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
            <Row>
                <div className="col-12">
                    <article className="blog-card">
                        <div class ="blog-card_outline">
                        <span> <img src={img1} alt=" Profile image" style={{width:"20px"}, {height:"20px"}}/>  User1 shared a post</span>
                        <div className="blog-card__info">            
                            <img src={img2} alt="Unfinished" width="200" height="300"/>
                            <a href="#" className="addtowishlist"><span>+ Add to Wish List</span></a>
                            <h5>Unfinished By Priyanka Chopra</h5>
                            <p>
                                <a href="#" className="icon-link mr-3"><i className="fa fa-pencil-square-o"></i> Priyanka’s ‘Unfinished’ is Measured, Engaging & Full of Humour</a>
                            </p>
                            <p>In spite of having been one of the most famous faces in the country, she didn’t resist doing multiple auditions or walking into the offices of media houses to introduce herself. In her memoir Unfinished, Chopra Jonas writes, “I swallowed my pride and reminded myself constantly that just because I’d received recognition in one part of the world was no reason that I should automatically receive it elsewhere”.

                                    She writes about going for the Roc Nation pre-Grammys party only to realize that she wasn’t where all the A-listers were; the pep talk she gave herself in a toilet just before walking in to audition to play Alex Parrish in Quantico – which made her the first Indian-born woman to lead a prime-time network show in the United States; and, being a bundle of nerves before her first press event for the ABC show.
                
                            </p>
                        <span> 
                            <i onclick="myFunction(this)" className="fa fa-thumbs-up"> Like/Dislike</i>
                            <form className="comment-form" method="post" action=" ">
                                Comments: <textarea name="comment"></textarea><br></br>
                                <input name="submit" type="submit" value="submit"></input><br></br>
                                <input name="reset" type="reset" value="reset"></input>		
                            </form>
                        </span>
                        
                        </div>
                    </div>
                    </article>
                </div>
            </Row>
        </Container>

        {/* <section className="detail-page">
        <div className="container mt-5">  

        </div>
        </section> */}

        {/* <script>
            function myFunction(x) {
         //   x.classList.toggle("fa-thumbs-down");
            }
        </script> */}

    </React.Fragment >

    );
}
export default withRouter(NewsFeed);   

