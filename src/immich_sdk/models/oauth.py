"""OAuth-related DTOs."""

from pydantic import BaseModel, Field


class OAuthConfigDto(BaseModel):
    """OAuth authorize request (start flow)."""

    redirectUri: str = Field(..., description="OAuth redirect URI")
    state: str | None = Field(None, description="OAuth state parameter")
    codeChallenge: str | None = Field(None, description="OAuth code challenge (PKCE)")


class OAuthAuthorizeResponseDto(BaseModel):
    """OAuth authorize response (URL to redirect user)."""

    url: str = Field(..., description="OAuth authorization URL")


class OAuthCallbackDto(BaseModel):
    """OAuth callback (finish flow)."""

    url: str = Field(..., description="OAuth callback URL")
    state: str | None = Field(None, description="OAuth state parameter")
    codeVerifier: str | None = Field(None, description="OAuth code verifier (PKCE)")


class OAuthMobileRedirectDto(BaseModel):
    """OAuth mobile redirect request."""

    url: str = Field(..., description="Redirect URL")
