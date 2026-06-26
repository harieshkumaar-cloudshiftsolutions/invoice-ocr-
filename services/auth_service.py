from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import User
from schemas.user import UserRegister, UserLogin
from core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, user: UserRegister):
    """
    Register a new user.
    """

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Create new user
    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, user: UserLogin):
    """
    Authenticate user and generate JWT token.
    """

    # Check if user exists
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Generate JWT access token
    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }