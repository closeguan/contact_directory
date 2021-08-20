#!"C:\Strawberry\perl\bin\perl.exe" 

use strict;
use warnings;
use DBI;
use CGI;
use JSON;
use Encode;
use Data::Dumper;

my $cgi = CGI->new;
print $cgi->header('text/html;charset=UTF-8');



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


# sql 欄位與值的設定
my $table="list";
my $attribute='name';
#my $search_name = "<script>'\" or 1=1"; 
#my $search_name = "珊迪"; 
my  $search_name = $cgi->param('name');   # 要做跳脫


### SQL query here
my $sql = <<EOF; 
			SELECT user, name, phone, email 
			FROM $table WHERE $attribute = ? 
EOF


my $sth = $dbh->prepare($sql);
 
### execute the query
$sth->execute($search_name);


## DB msg 
my $msg = $sth->errstr;              # DB 的error 錯誤輸出都會這裡
my $statement = $dbh->{Statement};  # sql指令的一種取法


## store sql data inti perl  
my @output;
while(my $ref = $sth->fetchrow_hashref()) {  
  push @output, $ref;
}

$dbh->disconnect();

## print in JSON
my $JSON=encode_json( \@output );     # encode_json() 含有UTF-8字符會有亂碼
#my $utf8_JSON=decode_utf8($JSON); 


$JSON =~ s/\[\{//g;
$JSON =~ s/\}\]//g;
$JSON =~ s/:]//g;
my @tmp=split/,/,$JSON;

my ($name, $user, $phone, $email);
foreach(@tmp){
	my @data=split/:/,$_;
	if($data[0] =~ /name/){
		$name = $data[1];
	}elsif($data[0] =~ /user/){
		$user = $data[1];
	}elsif($data[0] =~ /phone/){
		$phone = $data[1];
	}elsif($data[0] =~ /email/){
		$email = $data[1];
		
	}
}

my %rec_hash = (emailPERL => $email,
				  userPERL => $user,
				  namePERL => $name,
				  phonePERL => $phone,
				  msgPERL => $msg);



my $json = encode_json \%rec_hash;
my $utf8_json=decode_utf8($json);
print "$utf8_json\n";








