#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <vector>
int main(int argc,char**argv){
 if(argc!=5)return 2;
 int k=std::atoi(argv[1]),m=std::atoi(argv[2]),N=std::atoi(argv[3]);
 std::vector<unsigned char> q((size_t)(N+1)*(k+1),1);
 for(int n=1;n<=N;n++){
  std::vector<int> losing_children;
  for(int r=1;r<=std::min(n,k);r++)if(q[(size_t)(n-r)*(k+1)+r])losing_children.push_back(r);
  q[(size_t)n*(k+1)]=losing_children.empty();
  for(int s=1;s<=k;s++){
   bool losing=true;
   for(int r:losing_children)if(std::abs(r-s)>m){losing=false;break;}
   q[(size_t)n*(k+1)+s]=losing;
  }
 }
 std::ofstream f(argv[4],std::ios::binary);f.write((char*)q.data(),q.size());return !f;
}
