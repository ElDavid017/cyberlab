# SECURITY.md - Lab Practice No. 4
**Student:** David Guerrero
**Course:** Ethical Hacking - Eighth Semester
**University:** ULEAM, Extension El Carmen

---

## Q0: Why is an unauthenticated incident tracker a security problem?

If anyone can open /incidents/ without logging in, then an attacker who finds the URL can see all the reported vulnerabilities of the organization. That basically gives them a roadmap of what systems are broken. It's one of the worst things you can expose publicly.

## Q1: User model vs UserProfile — why OneToOneField?

Django's built-in User handles everything related to authentication (username, password, sessions). UserProfile is where we put extra stuff that Django doesn't know about by default, like our role field. We use OneToOneField because each user should have exactly one profile and vice versa. If we changed Django's User model directly we'd have to replace all of Django's auth system which is way more complicated.

## Q2: Purpose of ?next= and open redirect risk

When Django sends you to the login page because you tried to access a protected route, it saves where you were trying to go in the ?next= parameter. After logging in it takes you there. The security problem is if Django doesn't check that the next URL is on the same site, an attacker could send someone a link like /accounts/login/?next=http://evil.com and after the user logs in they get sent to the attacker's site. That's called an open redirect and it's commonly used in phishing.

## Q3: Authentication vs Authorization — concrete examples from the lab

Authentication is proving who you are. In this lab it's the login form checking your username and password.

Authorization is checking what you're allowed to do once you're logged in. In this lab the update and delete views check if your profile has role='admin' before letting you in.

If you skip authorization, any logged-in user (including analysts) could just go to /incidents/1/edit/ and change anything they want.

## Q4: commit=False and mass assignment risk

We use commit=False so we can set reported_by = request.user in the server before saving to the database. If instead we had a hidden field in the HTML form for reported_by, anyone could open DevTools, change the value, and submit the form pretending to be a different user. That's a mass assignment attack. Using commit=False means the user never controls that field.

## Q5: Why template hiding is NOT enough security

Hiding the Edit and Delete buttons in the template only changes what's displayed in the browser. Someone can still type /incidents/1/edit/ directly in the address bar and get to the view. This is called forced browsing or IDOR. The actual protection has to happen in the view function itself with the role check, not in the HTML.

## Q6 (Bonus): Brute-force attacks and django-axes mitigation

A brute-force attack is when someone writes a script to try thousands of username/password combinations against the login form until one works. django-axes tracks how many failed login attempts come from an IP and blocks it after AXES_FAILURE_LIMIT failures. If you set the limit too low (like 2 or 3) real users who just mistype their password get locked out. One other method to protect the login is adding a CAPTCHA so automated scripts can't submit the form at all.
