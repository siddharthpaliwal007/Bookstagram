import React from 'react';
import { Link } from 'react-router-dom';
import { withRouter } from 'react-router';

import logo from '../../assets/images/logo.png';

const Sidebar = () => {
  const userType = localStorage.getItem('userType');;

  return (
    <div class='sidebar'>
      <div class='brand-logo'>
        <a href='index.html'>
          <img src={logo} alt='logo' height="75px" width="75px" />
        </a>
      </div>
      <div class='menu'>
      { userType == "reader"?
        <ul>
          <li>
            <Link
              to="/home"
              data-toggle='tooltip'
              data-placement='right'
              title='Home'
            >
              <span>
                <i class='icofont-ui-home'></i>
              </span>
            </Link>
          </li>
          <li>
            <Link
              to="/my-books"
              data-toggle='tooltip'
              data-placement='right'
              title='My book Shelf'
            >
              <span>
                <i class='icofont-library'></i>
              </span>
            </Link>
          </li>
          <li>
            <Link
              to="/book-list"
              data-toggle='tooltip'
              data-placement='right'
              title='List Of Books'
            >
              <span>
                <i class='icofont-book'></i>
              </span>
            </Link>
          </li>

          <li>
            <Link
              to="/my-friends"
              data-toggle='tooltip'
              data-placement='right'
              title='My Friends'
            >
              <span>
                <i class='icofont-ui-user-group'></i>
              </span>
            </Link>
          </li>
          <li class='logout'>
            <a href='signin.html' data-toggle='tooltip' data-placement='right' title='Signout'>
              <span>
                <i class='icofont-power'></i>
              </span>
            </a>
          </li>
        </ul> :
        <ul>
        <li>
          <Link
            to="/"
            data-toggle='tooltip'
            data-placement='right'
            title='Home'
          >
            <span>
              <i class='icofont-ui-home'></i>
            </span>
          </Link>
        </li>
        <li>
          <Link
            to="/uploadbook"
            data-toggle='tooltip'
            data-placement='right'
            title='upload a book'
          >
            <span>
              <i class='icofont-library'></i>
            </span>
          </Link>
        </li>
        <li class='logout'>
          <a href='signin.html' data-toggle='tooltip' data-placement='right' title='Signout'>
            <span>
              <i class='icofont-power'></i>
            </span>
          </a>
        </li>
      </ul>
      }

        <p class='copyright'>
          &#169; <a href='#'>Bookstagram INC</a>
        </p>
      </div>
    </div>
  );
};

export default withRouter(Sidebar);
