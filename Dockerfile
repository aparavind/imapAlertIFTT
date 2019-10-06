FROM alpine
RUN apk add --update perl && rm -rf /var/cache/apk/*
RUN apk update
RUN apk add gcc g++ make patch perl perl-dev curl wget
RUN curl -L http://xrl.us/cpanm > /bin/cpanm && chmod +x /bin/cpanm
RUN cpanm MIME::Lite
RUN cpanm String::Random
RUN cpanm Authen::SASL
RUN mkdir /usr/local/lib/perl5/site_perl/ECM
COPY smtpmail /bin/smtpmail
RUN chmod +x /bin/smtpmail
COPY Mail.pm /usr/local/lib/perl5/site_perl/ECM/
