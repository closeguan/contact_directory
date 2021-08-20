#!"C:\Strawberry\perl\bin\perl.exe" 

use strict;
use warnings;
use DBI;
use JSON;
use Encode;
use CGI qw(:standard);

print header(-charset => 'utf-8'); # 定義表頭，並給utf8編碼

## input from ajax
my $cgi = CGI->new;
my	$user = $cgi->param('user'); 
my  $name = $cgi->param('name');
my  $email = $cgi->param('email');
my  $phone = $cgi->param('phone');

## test data
#my	$user = "qwert"; 
#my  $name = "QWERT";
#my  $email = "qwewqe\@gmail.com";
#my  $phone = "67878";

my @array = ($user, $name, $email, $phone);


### MySQL connect details
my $db = "project";
my $host = "localhost";
my $username = "root";
my $password = "1234";
 
### connect to MySQL database
my $dbh = DBI->connect ("DBI:mysql:database=$db:host=$host", $username, $password) 
						or die "Could not connect to database: $DBI::errstr\n";
$dbh->{mysql_enable_utf8} = 1;
$dbh->do('set names "UTF8"');

##########################################
#    insert data into the list table
##########################################
my $table="list";
my $sql = "DELETE FROM $table WHERE name=?";
my $stmt = $dbh->prepare($sql);
$stmt->execute($user);


##  after insert : select all t print
$stmt->disconnect();


#convert  data to JSON
my $op = JSON -> new -> utf8 -> pretty(1);
my $json = $op -> encode({
    emailPERL => $email,
    userPERL => $user,
	namePERL => $name,
	phonePERL => $phone,
});

print $json;


