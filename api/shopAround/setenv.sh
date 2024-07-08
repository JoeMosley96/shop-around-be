if [ "$1" == "test" ]; then
    export DJANGO_ENV=testing
    psql -f create_db.sql
    echo "Environment set to testing"
elif [ "$1" == "production" ]; then
    export DJANGO_ENV=production
    echo "Environment set to production"
else 
    echo "Please use test or production"
fi